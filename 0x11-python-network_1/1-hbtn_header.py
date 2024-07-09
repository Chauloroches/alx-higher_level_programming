#!/usr/bin/python3
# Response header value #0

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    
    with urllib.request.urlopen(url) as response:
        headers = response.getheaders()
        for header in headers:
            if header[0] == "X-Request-Id":
                print(header[1])
                break
