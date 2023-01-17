#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests
    url = "https://alx-intranet.hbtn.io/status"
    r = requests.get(url)
    body_response = r.text
    print("Body response:")
    print("\t- type: {}".format(type(body_response)))
    print("\t- content: {}".format(body_response))
