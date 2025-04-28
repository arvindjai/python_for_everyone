import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://arvindjaiswal179.atlassian.net/rest/api/3/project"

API_TOKEN=""

auth = HTTPBasicAuth("arvind.jaiswal179@outlook.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

output = json.loads(response.text)
for n in range(0,2):
  name = output[n]["name"]

  print(name)