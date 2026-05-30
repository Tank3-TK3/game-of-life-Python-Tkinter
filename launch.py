import http.server
import threading
import subprocess
import os
import sys

PORT = 8765
os.chdir(os.path.dirname(os.path.abspath(__file__)))

handler = http.server.SimpleHTTPRequestHandler
handler.log_message = lambda *_: None

server = http.server.HTTPServer(('localhost', PORT), handler)
threading.Thread(target=server.serve_forever, daemon=True).start()

url = f'http://localhost:{PORT}/index.html'

# WSL2: open in Windows browser
try:
    subprocess.run(['powershell.exe', '-Command', f"Start-Process '{url}'"],
                   capture_output=True, timeout=5)
except Exception:
    try:
        subprocess.run(['cmd.exe', '/c', f'start {url}'], capture_output=True, timeout=5)
    except Exception:
        import webbrowser
        webbrowser.open(url)

print(f"Game of Life v3.0  →  {url}")
print("Ctrl+C para salir.")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nCerrado.")
