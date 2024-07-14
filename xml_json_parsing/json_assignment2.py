import urllib.request, urllib.parse
import ssl, json
import urllib.response

# Ignore SSL Certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'
address = input('Enter Location: ')
address = address.strip()
param = dict()
param['q'] = address

url = serviceurl + urllib.parse.urlencode(param)
print("Retreving :",url)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print("Retrevied",len(data),'character')

js = json.loads(data)
print(js['features'][0]['properties']['plus_code'])
