"""hello-aws client: runs on the PC and calls the server on EC2.

Usage: python3 client.py <EC2_PUBLIC_IP>
"""

import sys
import urllib.error
import urllib.request

PORT = 8080
TIMEOUT_SECONDS = 10


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 client.py <EC2_PUBLIC_IP>")
        sys.exit(1)

    url = f"http://{sys.argv[1]}:{PORT}/"
    try:
        with urllib.request.urlopen(url, timeout=TIMEOUT_SECONDS) as response:
            print(response.read().decode("utf-8"), end="")
    except (urllib.error.URLError, TimeoutError) as error:
        print(f"Could not reach {url}: {error}")
        print("Is server.py running? Has your home IP or the instance IP changed?")
        print("See docs/troubleshooting.md")
        sys.exit(1)


if __name__ == "__main__":
    main()
