import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# url = 'http://py4e-data.dr-chuck.net/comments_42.html'
url = ' http://py4e-data.dr-chuck.net/comments_1949661.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retreving numbers from tables.
tags = soup.find_all('span',None)
sum = 0
for tag in tags:
    num = tag.contents[0]
    sum += int(num)
print(sum)