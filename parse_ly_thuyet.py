import os
import json
import glob
import re

def parse_ly_thuyet_files(out_json):
    chapters = []
    
    # Đọc các file trong thư mục data/LSD/
    md_files = glob.glob('data/LSD/*_ly_thuyet.md')
    # Sort alphabetically works perfectly for 'chuong_mo_dau' and 'giai_doan_YYYY_YYYY'
    md_files.sort()
    
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else os.path.basename(md_file)
        
        base_name = os.path.basename(md_file).replace('_ly_thuyet.md', '')
        
        chapters.append({
            "id": base_name,
            "title": title,
            "content": content
        })
        
    data = {
        "subject": "Lý Thuyết Lịch Sử Đảng",
        "chapters": chapters
    }
    
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    parse_ly_thuyet_files('data/lythuyet_LSD.json')
    print("Xong parse lý thuyết")
