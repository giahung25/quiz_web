import os
import json
import glob
import re

def parse_trac_nghiem_files(json_file):
    # Đảm bảo file tồn tại để đọc, nếu không thì tạo data mới
    if os.path.exists(json_file):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = {"questions": [], "sections": []}
    else:
        data = {"questions": [], "sections": []}
    
    questions = data.get('questions', [])
    sections = data.get('sections', [])
    
    # Lấy danh sách file markdown
    md_files = glob.glob('data/LSD/*_trac_nghiem.md')
    md_files.sort()
    
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract title
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        section_title = title_match.group(1).strip() if title_match else os.path.basename(md_file)
        
        base_name = os.path.basename(md_file).replace('_trac_nghiem.md', '')
        
        # Tạo section_key dễ đọc
        if base_name == 'chuong_mo_dau':
            section_key = "Chương mở đầu: Trắc nghiệm"
        elif base_name.startswith('giai_doan_'):
            parts = base_name.split('_')
            if len(parts) >= 4:
                section_key = f"Giai đoạn {parts[2]}-{parts[3]}: Trắc nghiệm"
            else:
                section_key = f"{base_name}: Trắc nghiệm"
        else:
            section_key = f"{base_name}: Trắc nghiệm"
        
        # Split by questions
        q_blocks = re.split(r'\*\*Câu \d+:\*\*', content)
        
        count = 0
        for block in q_blocks[1:]: # Skip the first part before the first question
            lines = [line.strip() for line in block.strip().split('\n') if line.strip()]
            if not lines: continue
            
            question_text = lines[0]
            options = []
            answer = ""
            explanation = ""
            
            for line in lines[1:]:
                if line.startswith('A.') or line.startswith('B.') or line.startswith('C.') or line.startswith('D.'):
                    options.append(line)
                elif line.startswith('*Đáp án:'):
                    ans_char = line.replace('*Đáp án:', '').replace('*', '').strip()
                    # Find the full option text
                    for opt in options:
                        if opt.startswith(ans_char + '.'):
                            answer = opt
                            break
                elif line.startswith('*Giải thích:'):
                    explanation = line.replace('*Giải thích:', '').replace('*', '').strip()
            
            # Lọc các câu hỏi rác
            is_junk = False
            for text in [question_text] + options:
                lower_text = text.lower()
                if "biến thể" in lower_text or "nhận định sai lầm" in lower_text or "nội dung sai lệch" in lower_text:
                    is_junk = True
                    break
            
            if is_junk:
                continue

            if question_text and options and answer:
                q_obj = {
                    "question": question_text,
                    "options": options,
                    "answer": answer,
                    "explanation": explanation,
                    "section": section_key,
                    "sectionLabel": section_title
                }
                questions.append(q_obj)
                count += 1
                
        # Update sections
        existing_section = next((s for s in sections if s['key'] == section_key), None)
        if existing_section:
            existing_section['count'] += count
        else:
            sections.append({
                "key": section_key,
                "label": f"{section_title} ({count} câu)",
                "count": count
            })
            
    # Update total Q
    data['totalQ'] = len(questions)
    
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    parse_trac_nghiem_files('data/tracnghien_LSD.json')
    print("Xong parse trắc nghiệm")
