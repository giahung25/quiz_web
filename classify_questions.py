import json
import re
import time

try:
    import vertexai
    from vertexai.generative_models import GenerativeModel, SafetySetting, Part
    VERTEX_AVAILABLE = True
except ImportError:
    VERTEX_AVAILABLE = False

def get_chapter_auto(question, options, answer):
    text = (question + " " + " ".join(options) + " " + answer).lower()
    
    # 1. Các trường hợp đặc biệt không thể dựa vào năm chung chung
    if "sau cách mạng tháng tám" in text or "sau cmt8" in text:
        return "chuong_2"
    if "trước cách mạng tháng tám" in text or "trước cmt8" in text:
        return "chuong_1"
        
    # 2. Tìm tất cả các năm (4 chữ số)
    years = [int(y) for y in re.findall(r'\b(18\d{2}|19\d{2}|20\d{2})\b', text)]
    if years:
        max_year = max(years)
        min_year = min(years)
        
        # Nếu có năm sau 1975 -> Chương 3
        if max_year > 1975:
            return "chuong_3"
            
        # Nếu năm thấp nhất từ 1946 trở đi (và lớn nhất <= 1975) -> Chương 2
        if min_year >= 1946:
            return "chuong_2"
            
        # Nếu năm lớn nhất <= 1944 -> Chương 1
        if max_year < 1945:
            return "chuong_1"
            
        # Nếu có năm 1945, cần phân biệt dựa vào ngữ cảnh (trước hay sau CMT8)
        if 1945 in years:
            c2_1945 = ["kháng chiến", "chống pháp", "đối phó với quân tưởng", "hiệp định sơ bộ", "tạm ước", "toàn quốc kháng chiến", "diệt cộng, cầm hồ"]
            if any(k in text for k in c2_1945):
                return "chuong_2"
            c1_1945 = ["tổng khởi nghĩa", "giành chính quyền", "nhật - pháp bắn nhau", "cao trào kháng nhật", "hội nghị lần thứ viii", "hội nghị 8", "đội việt nam tuyên truyền", "tân trào", "quốc dân đại hội", "khởi nghĩa", "cách mạng tháng tám", "ủy ban dân tộc giải phóng", "nhật đầu hàng"]
            if any(k in text for k in c1_1945):
                return "chuong_1"
            # Mặc định năm 1945 đưa vào chương 1 (theo yêu cầu của user)
            return "chuong_1"

    # 3. Phân loại qua từ khoá (nếu không có năm)
    c3_keywords = ["đổi mới", "đại hội vi ", "đại hội vii", "đại hội viii", "đại hội ix", "đại hội x ", "đại hội xi ", "đại hội xii", "đại hội xiii", "kinh tế thị trường", "quá độ lên cnxh", "công nghiệp hóa", "hiện đại hóa"]
    if any(k in text for k in c3_keywords):
        return "chuong_3"
        
    c2_keywords = ["chống mỹ", "điện biên phủ", "giơ-ne-vơ", "pa-ri", "đồng khởi", "ngô đình diệm", "chiến tranh đặc biệt", "chiến tranh cục bộ", "việt nam hoá chiến tranh", "mậu thân", "đường 9", "12 ngày đêm", "giải phóng miền nam", "30/4/1975", "đại hội ii ", "đại hội iii ", "kế hoạch 5 năm", "miền bắc", "miền nam"]
    if any(k in text for k in c2_keywords):
        return "chuong_2"
        
    c1_keywords = ["nguyễn ái quốc", "quốc tế cộng sản", "hội việt nam cách mạng thanh niên", "cương lĩnh chính trị đầu tiên", "xô viết nghệ tĩnh", "mặt trận dân chủ", "đường kách mệnh", "bản án chế độ thực dân", "thành lập đảng", "cộng sản đảng", "khai thác thuộc địa", "đông dương"]
    if any(k in text for k in c1_keywords):
        return "chuong_1"
        
    # Không thể xác định -> Đẩy cho AI
    return None 

def call_vertex_ai(batch, sections_map):
    if not VERTEX_AVAILABLE:
        return []
        
    # User yêu cầu "locations: global" và project id "tool-dich-thuat"
    try:
        vertexai.init(project="tool-dich-thuat", location="global")
        model = GenerativeModel("gemini-2.5-flash-lite")
    except Exception as e:
        print("Lỗi khởi tạo Vertex AI:", e)
        return []
    
    prompt = "Bạn là chuyên gia Lịch sử Đảng. Hãy phân loại các câu hỏi sau vào 1 trong 3 chương dựa vào ngữ cảnh thời gian:\n"
    prompt += "- chuong_1: (1930 - 1945)\n"
    prompt += "- chuong_2: (1945 - 1975)\n"
    prompt += "- chuong_3: (1975 - nay)\n"
    prompt += "Chú ý: Những sự kiện liên quan trực tiếp đến năm 1945 (như Khởi nghĩa, CMT8, Nạn đói) thường thuộc chuong_1. Còn 'Sau CMT8', 'kháng chiến chống Pháp/Mỹ' thuộc chuong_2.\n\n"
    prompt += "CHỈ TRẢ VỀ một mảng JSON có định dạng: [{\"id\": <id>, \"section\": \"chuong_X\"}]. KHÔNG IN RA BẤT KỲ VĂN BẢN NÀO KHÁC.\n\n"
    
    for item in batch:
        prompt += f"ID: {item['id']}\nQ: {item['question']}\nA: {item['answer']}\n\n"
        
    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        # Clean markdown
        if text.startswith("```json"): text = text[7:-3].strip()
        elif text.startswith("```"): text = text[3:-3].strip()
        
        return json.loads(text)
    except Exception as e:
        print(f"Lỗi khi gọi AI hoặc parse JSON: {e}")
        # In ra để debug
        try: print("Raw text:", text)
        except: pass
        return []

def process():
    file_path = 'data/tracnghiem_LSD_chuong_gemini.json'
    print(f"Đang đọc file {file_path}...")
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    
    sections = {s['key']: s['label'] for s in data['sections']}
    questions = data['questions']
    
    ambiguous = []
    
    # Bước 1: Phân loại bằng code heuristic
    for i, q in enumerate(questions):
        auto_chap = get_chapter_auto(q['question'], q.get('options', []), q['answer'])
        if auto_chap:
            q['section'] = auto_chap
            q['sectionLabel'] = sections[auto_chap]
        else:
            ambiguous.append({'id': i, 'question': q['question'], 'answer': q['answer']})
            
    print(f"Tổng số câu: {len(questions)}")
    print(f"Đã phân loại tự động bằng Rule (Python): {len(questions) - len(ambiguous)}")
    print(f"Số câu cần dùng Vertex AI (Gemini 2.5 Flash-lite): {len(ambiguous)}")
    
    if len(ambiguous) > 0 and not VERTEX_AVAILABLE:
        print("LƯU Ý: Thư viện `google-cloud-aiplatform` chưa được cài đặt.")
        print("Hãy chạy `pip install google-cloud-aiplatform` và cấu hình Google Cloud CLI để dùng AI.")
        
    # Bước 2: Gọi Vertex AI cho các câu không rõ ràng
    if len(ambiguous) > 0 and VERTEX_AVAILABLE:
        batch_size = 100
        batches = [ambiguous[i:i + batch_size] for i in range(0, len(ambiguous), batch_size)]
        
        for idx, batch in enumerate(batches):
            print(f"Đang xử lý bằng AI batch {idx + 1}/{len(batches)} (100 câu/batch)...")
            llm_results = call_vertex_ai(batch, sections)
            for res in llm_results:
                q_id = res.get('id')
                sec = res.get('section')
                if q_id is not None and sec in sections:
                    questions[q_id]['section'] = sec
                    questions[q_id]['sectionLabel'] = sections[sec]
            
            # Tạm dừng 3s để tránh bị rate limit (Quota)
            time.sleep(3) 
            
            # Ghi tạm ra file để lỡ lỗi giữa chừng không bị mất dữ liệu
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                
    # Lưu lại file cuối cùng
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Hoàn tất! Đã lưu toàn bộ kết quả vào file json.")

if __name__ == "__main__":
    process()