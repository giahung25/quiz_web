import http.server
import socketserver
import webbrowser
import os

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"🚀 Server đang chạy tại: http://localhost:{PORT}")
        print("Mẹo: Nhấn Ctrl+C để dừng server.")
        webbrowser.open(f"http://localhost:{PORT}/index.html")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Đang dừng server...")
            httpd.server_close()

if __name__ == "__main__":
    run()
