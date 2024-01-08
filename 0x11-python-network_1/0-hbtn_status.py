#!/usr/bin/python3
"""
Fetches a website URI with urllib
"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
       the_page = response.read()
       utf8_content = the_page.decode('utf-8')
    print("Body response:")
    print(f"\t- type: {type(the_page)}")
    print("\t- content: {}".format(the_page))
    print("\t- utf8 content: {}".format(utf8_content))
