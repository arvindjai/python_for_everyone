import urllib.request, urllib.parse
import ssl, json

serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# while True:
address = input("Enter location: ")
# if len(address) < 1:
#     break
address = address.strip()
params = dict()
params['q'] = address

url = serviceurl + urllib.parse.urlencode(params)
print("Retreiving",url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()

print("Retreved ", len(data), 'Characters' )
print(type(data))

js = json.loads(data)
# print(json.dumps(js))
print(json.dumps(js['features'][0]['properties']['lat']))
print(json.dumps(js['features'][0]['properties']['formatted']))