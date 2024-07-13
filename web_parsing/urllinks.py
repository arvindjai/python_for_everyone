import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.verify_mode = False
ctx.check_hostname = ssl.CERT_NONE

url = input('Enter URL-  ')
# http://www.dr-chuck.com/page1.htm
# https://pypi.org/project/beautifulsoup4/
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")
# print(soup)

# Retreive all of the anchor tags
tags = soup('a')
count = 0
for tag in tags:
    links = tag.get('href', None)
    if links:
        count += 1
        print(links)
print(f'Total links in site {url} : {count}')
