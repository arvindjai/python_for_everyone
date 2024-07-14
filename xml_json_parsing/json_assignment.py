import urllib.request, urllib.parse
import ssl, json

# ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input("Enter URL: ")
# URL 1: http://py4e-data.dr-chuck.net/comments_42.json
# URL 2: http://py4e-data.dr-chuck.net/comments_1949664.json
url = 'http://py4e-data.dr-chuck.net/comments_1949664.json'
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

js = json.loads(data)
# print(json.dumps(js))
# print(js['comments'])

num = list()
for item in js['comments']:
    count_str = item['count']
    num.append(int(count_str))

print(sum(num))