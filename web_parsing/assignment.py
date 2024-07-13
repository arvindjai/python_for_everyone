import urllib.request, urllib.parse, urllib.error
from  bs4 import BeautifulSoup
import re

url = 'http://py4e-data.dr-chuck.net/comments_42.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

tags  = soup('span')
number = list()
for tag in tags:
    num = int(tag.string)
    number.append(num)
print(sum(number))