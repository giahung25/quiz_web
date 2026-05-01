import os
import glob
import re

def cleanup_md_files():
    md_files = glob.glob('data/LSD/*.md')
    
    for file_path in md_files:
        print(f"Processing {file_path}...")
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Tách nội dung thành các phần: Header và các khối câu hỏi
        # Giả sử các câu hỏi bắt đầu bằng **Câu n:**
        parts = re.split(r'(\*\*Câu \d+:\*\*)', content)
        
        if len(parts) < 2:
            continue
            
        new_content = parts[0] # Giữ lại phần header trước câu hỏi đầu tiên
        
        removed_count = 0
        for i in range(1, len(parts), 2):
            q_header = parts[i]
            q_body = parts[i+1] if i+1 < len(parts) else ""
            
            # Kiểm tra xem thân câu hỏi có chứa từ "biến thể" (không phân biệt hoa thường) không
            if re.search(r'biến thể', q_header + q_body, re.IGNORECASE):
                removed_count += 1
                continue # Bỏ qua khối này
            
            new_content += q_header + q_body
            
        if removed_count > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  Removed {removed_count} junk questions from {file_path}")
        else:
            print(f"  No junk questions found in {file_path}")

if __name__ == "__main__":
    cleanup_md_files()
