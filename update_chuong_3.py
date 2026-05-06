import json
import re
import os

def update_chuong_3():
    json_path = 'data/tracnghien_LSD.json'
    md_path = 'data/LSD/chuong_3_trac_nghiem.md'
    section_key = 'chuong_3: Trắc nghiệm'
    
    if not os.path.exists(json_path) or not os.path.exists(md_path):
        print("Không tìm thấy file.")
        return

    # 1. Đọc JSON
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 2. Xóa các câu hỏi cũ của chương 3
    data['questions'] = [q for q in data['questions'] if q.get('section') != section_key]
    
    # 3. Đọc và parse file Markdown mới
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    section_title = title_match.group(1).strip() if title_match else "CHƯƠNG 3: ĐẢNG LÃNH ĐẠO CẢ NƯỚC QUÁ ĐỘ LÊN CHỦ NGHĨA XÃ HỘI VÀ TIẾN HÀNH CÔNG CUỘC ĐỔI MỚI (Từ năm 1975 đến nay)"
    
    # Split by questions
    q_blocks = re.split(r'\*\*Câu \d+:\*\*', content)
    
    new_questions = []
    for block in q_blocks[1:]:
        lines = [line.strip() for line in block.strip().split('\n') if line.strip()]
        if not lines: continue
        
        question_text = lines[0]
        options = []
        answer = ""
        explanation = ""
        
        for line in lines[1:]:
            if re.match(r'^[A-D]\.', line):
                options.append(line)
            elif line.startswith('*Đáp án:'):
                ans_char = line.replace('*Đáp án:', '').replace('*', '').strip()
                for opt in options:
                    if opt.startswith(ans_char + '.'):
                        answer = opt
                        break
            elif line.startswith('*Giải thích:'):
                explanation = line.replace('*Giải thích:', '').replace('*', '').strip()
        
        # Lọc câu hỏi rác
        is_junk = False
        for text in [question_text] + options:
            lower_text = text.lower()
            if "biến thể" in lower_text or "nhận định sai lầm" in lower_text or "nội dung sai lệch" in lower_text:
                is_junk = True
                break
        
        if is_junk: continue

        if question_text and options and answer:
            q_obj = {
                "question": question_text,
                "options": options,
                "answer": answer,
                "explanation": explanation,
                "section": section_key,
                "sectionLabel": section_title
            }
            new_questions.append(q_obj)
    
    # 4. Thêm câu hỏi mới vào danh sách
    data['questions'].extend(new_questions)
    
    # 5. Cập nhật sections info
    count = len(new_questions)
    section_found = False
    for s in data.get('sections', []):
        if s['key'] == section_key:
            s['count'] = count
            s['label'] = f"{section_title} ({count} câu)"
            section_found = True
            break
    
    if not section_found:
        if 'sections' not in data: data['sections'] = []
        data['sections'].append({
            "key": section_key,
            "label": f"{section_title} ({count} câu)",
            "count": count
        })
    
    # 6. Cập nhật tổng số câu hỏi
    data['totalQ'] = len(data['questions'])
    
    # 7. Ghi đè file JSON
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Đã cập nhật xong chương 3: {count} câu hỏi.")

if __name__ == '__main__':
    update_chuong_3()
