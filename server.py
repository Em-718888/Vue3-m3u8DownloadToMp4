#!/usr/bin/env python3
import http.server
import socketserver
import os

# 设置端口
PORT = 8000

# 切换到当前目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # FFmpeg.wasm 需要的关键安全头
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        # 允许SharedArrayBuffer和跨域资源
        self.send_header('Cross-Origin-Resource-Policy', 'cross-origin')
        # 添加CORS头支持外部资源
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"服务器运行在: http://localhost:{PORT}")
        print(f"本地访问: http://localhost:{PORT}/simple.html")
        print(f"局域网访问: http://10.10.100.80:{PORT}/simple.html")
        print()
        print("其他设备访问步骤:")
        print("1. 确保设备在同一局域网")
        print("2. 打开浏览器访问: http://10.10.100.80:8000/simple.html")
        print("3. 如无法访问，请检查防火墙设置")
        print()
        print("按 Ctrl+C 停止服务器")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n服务器已停止")