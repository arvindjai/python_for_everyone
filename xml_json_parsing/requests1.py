import requests

url = 'https://www.ibm.com'
r = requests.get(url)
print(r.status_code)
print(r.request.headers)
print(r.request.body)
print(r.headers)
print(r.headers['date'])
print(r.headers['Content-Type'])
