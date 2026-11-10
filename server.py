"""hello-aws server: runs on EC2 and answers every GET with "hello world".

Usage: python3 server.py
"""

from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "0.0.0.0"  # listen on all network interfaces, so the internet can reach it
PORT = 8080


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b"hello world\n"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main():
    server = HTTPServer((HOST, PORT), HelloHandler)
    print(f"Listening on {HOST}:{PORT} (Ctrl+C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
