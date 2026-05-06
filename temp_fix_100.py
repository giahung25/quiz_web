
import json
import os

# Sử dụng đường dẫn tương đối từ gốc dự án
file_path = 'data/tracnghiem_LSD_chuong_gemini.json'

if not os.path.exists(file_path):
    print(f"File not found: {os.path.abspath(file_path)}")
    exit(1)

with open(file_path, 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

questions = data['questions']
changed_count = 0

section_map = {
    'chuong_1': 'CHƯƠNG 1 - LÃNH ĐẠO ĐẤU TRANH GIÀNH CHÍNH QUYỀN (1930 - 1945)',
    'chuong_2': 'CHƯƠNG 2 - LÃNH ĐẠO HAI CUỘC KHÁNG CHIẾN (1945 - 1975)',
    'chuong_3': 'CHƯƠNG 3 - QUÁ ĐỘ LÊN CNXH VÀ ĐỔI MỚI (1975 - NAY)'
}

for i in range(min(100, len(questions))):
    q = questions[i]
    q_text = q['question'].lower()
    old_section = q.get('section')
    
    new_section = None
    
    # Ưu tiên Chương 3 cho các câu hỏi về Đại hội sau 1975 hoặc các khái niệm hiện đại
    if any(x in q_text for x in ['đại hội xi', 'đại hội vi', 'đại hội vii', 'đại hội viii', 'đại hội ix', 'đại hội x', 'đại hội xii', 'đại hội xiii', 'đổi mới', 'quá độ', 'văn kiện đại hội xi']):
        new_section = 'chuong_3'
    # Chương 2 cho giai đoạn kháng chiến và sau 1945
    elif any(x in q_text for x in ['1946', '1954', '1960', '1975', 'kháng chiến', 'điện biên phủ', 'hiệp định giơ-ne-vơ', 'hiệp định pari', 'miền bắc', 'xây dựng cnxh']):
         # Ngoại trừ 1945 chuẩn bị khởi nghĩa
         if '1945' in q_text and any(x in q_text for x in ['giành chính quyền', 'tổng khởi nghĩa', 'tháng tám', 'nhật đảo chính']):
             new_section = 'chuong_1'
         else:
             new_section = 'chuong_2'
    # Chương 1 cho giai đoạn trước và trong 1945 (giành chính quyền)
    elif any(x in q_text for x in ['đối tượng nghiên cứu', 'phương pháp', 'nhiệm vụ hàng đầu', 'chức năng', '1930', 'nguyễn ái quốc', 'hội nghị thành lập đảng', 'cương lĩnh chính trị đầu tiên', 'xô viết nghệ tĩnh', 'phong kiến', 'thực dân pháp xâm lược']):
        new_section = 'chuong_1'
    elif '1945' in q_text:
        if any(x in q_text for x in ['bảo vệ chính quyền', 'đối phó', 'tưởng', 'pháp xâm lược trở lại', 'hiệp định sơ bộ', 'tạm ước']):
            new_section = 'chuong_2'
        else:
            new_section = 'chuong_1'
    else:
        new_section = 'chuong_1'

    if new_section and new_section != old_section:
        q['section'] = new_section
        q['sectionLabel'] = section_map[new_section]
        changed_count += 1

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'SUCCESS: Changed {changed_count} questions.')
