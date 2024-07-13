import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# URL : https://py4e-data.dr-chuck.net/known_by_Fikret.html
# URL2 : http://py4e-data.dr-chuck.net/known_by_Elora.html
url = input('Enter URL: ')
count = int(input("Enter count: "))
position = int(input("Enter position: "))

names = []

while count > 0:
    print(f'Retrieving: {url}')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    anchor = soup('a')
    name = anchor[position-1].string
    names.append(name)
    url = anchor[position-1]['href']
    count -= 1
print(names[-1])