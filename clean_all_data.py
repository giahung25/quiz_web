import json
import os
import glob
import re

def is_junk(text):
    text = text.lower()
    return "biến thể" in text or "nhận định sai lầm" in text or "nội dung sai lệch" in text

def clean_json(file_path):
    if not os.path.exists(file_path):
        return
    print(f"Đang kiểm tra {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    questions = data.get('questions', [])
    original_count = len(questions)
    
    clean_questions = []
    sec_map = {}
    
    for q in questions:
        text = q.get('question', '') + ' ' + ' '.join(q.get('options', []))
        if not is_junk(text):
            clean_questions.append(q)
            sec = q.get('section', '')
            sec_map[sec] = sec_map.get(sec, 0) + 1
            
    data['questions'] = clean_questions
    data['totalQ'] = len(clean_questions)
    
    clean_sections = []
    for s in data.get('sections', []):
        count = sec_map.get(s['key'], 0)
        if count > 0:
            s['count'] = count
            # Cập nhật nhãn (ví dụ: "(129 câu)" thành số mới)
            s['label'] = re.sub(r'\(\d+\s*câu\)', f"({count} câu)", s.get('label', ''))
            clean_sections.append(s)
            
    data['sections'] = clean_sections
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    removed = original_count - len(clean_questions)
    print(f"  -> Đã xóa {removed} câu rác. Còn lại {len(clean_questions)} câu hợp lệ.")

def clean_md_files():
    md_files = glob.glob('data/LSD/*.md') + glob.glob('data/MangMayTinh/*.md')
    for file_path in md_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        parts = re.split(r'(\*\*Câu \d+:\*\*)', content)
        if len(parts) < 2:
            continue
            
        new_content = parts[0]
        removed_count = 0
        
        for i in range(1, len(parts), 2):
            q_header = parts[i]
            q_body = parts[i+1] if i+1 < len(parts) else ""
            
            if is_junk(q_header + q_body):
                removed_count += 1
                continue
            
            new_content += q_header + q_body
            
        if removed_count > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Đã xóa {removed_count} câu rác trong {os.path.basename(file_path)}")

if __name__ == "__main__":
    print("BẮT ĐẦU DỌN DẸP DỮ LIỆU RÁC...\n")
    clean_json('data/mangmaytinh.json')
    clean_json('data/tracnghien_LSD.json')
    print("\nĐang kiểm tra các file nguồn Markdown...")
    clean_md_files()
    print("\nHOÀN TẤT DỌN DẸP!")
