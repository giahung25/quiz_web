import os
import re

files = [
    r'D:\Download\Thi\quiz_web\data_web\chuong_mo_dau_trac_nghiem.md',
    r'D:\Download\Thi\quiz_web\data_web\chuong_3_trac_nghiem.md',
    r'D:\Download\Thi\quiz_web\data_web\giai_doan_1969_1975_trac_nghiem.md',
    r'D:\Download\Thi\quiz_web\data_web\giai_doan_1965_1968_trac_nghiem.md',
    r'D:\Download\Thi\quiz_web\data_web\giai_doan_1961_1965_trac_nghiem.md',
    r'D:\Download\Thi\quiz_web\data_web\giai_doan_1954_1960_trac_nghiem.md',
    r'D:\Download\Thi\quiz_web\data_web\giai_doan_1951_1954_trac_nghiem.md',
    r'D:\Download\Thi\quiz_web\data_web\giai_doan_1946_1950_trac_nghiem.md',
    r'D:\Download\Thi\quiz_web\data_web\giai_doan_1945_1946_trac_nghiem.md',
    r'D:\Download\Thi\quiz_web\data_web\chuong_1_trac_nghiem.md',
    r'D:\Download\Thi\quiz_web\data_web\chuong_2_trac_nghiem.md'
]
for f in files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            # Try to match different variations of **Câu X** or **Câu X.**
            count = len(re.findall(r'(?i)^\*\*\s*câu\s+\d+.*?\*\*', content, re.MULTILINE))
            print(f'{os.path.basename(f)}: {count}')
    else:
        print(f'{os.path.basename(f)}: File not found')
