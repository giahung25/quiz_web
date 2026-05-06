import http.server
import socketserver
import json
import os
import threading

PORT = 8000
DIRECTORY = "."
TARGET_FILE = 'tracnghiem_LSD_chuong_gemini.json'

# Khóa để tránh việc nhiều máy ghi vào file cùng một lúc gây hỏng file
file_lock = threading.Lock()

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_POST(self):
        if self.path == '/save-json':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data)
                content = data.get('content')
                
                with file_lock:
                    # Ghi đè trực tiếp vào file mục tiêu
                    with open(TARGET_FILE, 'w', encoding='utf-8-sig') as f:
                        json.dump(content, f, ensure_ascii=False, indent=2)
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'success', 'message': 'Đã cập nhật file gốc'}).encode())
                print(f"✅ [{self.client_address[0]}] Đã lưu thay đổi vào {TARGET_FILE}")
            except Exception as e:
                print(f"❌ Lỗi ghi file: {str(e)}")
                self.send_response(500)
                self.end_headers()
                self.wfile.write(str(e).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

# Sử dụng Threading để xử lý nhiều máy truy cập cùng lúc nhanh hơn
class ThreadingSimpleServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

with ThreadingSimpleServer(("", PORT), MyHandler) as httpd:
    print("\n" + "="*50)
    print(f"🚀 SERVER CHỈNH SỬA TẬP TRUNG ĐANG CHẠY")
    print(f"📍 File mục tiêu: {os.path.abspath(TARGET_FILE)}")
    print(f"🔗 Link máy chủ: http://localhost:{PORT}/dashboard_edit_lsd.html")
    
    # Lấy IP để hiển thị cho người dùng dễ copy
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try: s.connect(('8.8.8.8', 1)); ip = s.getsockname()[0]
    except: ip = "127.0.0.1"
    finally: s.close()
    
    print(f"🌐 Link máy khách: http://{ip}:{PORT}/dashboard_edit_lsd.html")
    print("="*50)
    print("📢 Nhấn Ctrl+C để dừng server.\n")
    httpd.serve_forever()
