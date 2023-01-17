#!/usr/bin/python3
"""
    take  a URL
    and email address, 
    sends a POST to URL with the email then displays the response.
"""

if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    r = requests.post(url, data)
    body = r.text
    print(body)
