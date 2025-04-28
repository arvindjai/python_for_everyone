import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://arvindjaiswal179.atlassian.net/rest/api/3/issue"

API_TOKEN=""

auth = HTTPBasicAuth("arvind.jaiswal179@outlook.com", API_TOKEN)

headers = {
"Accept": "application/json",
"Content-Type": "application/json"
}

payload = json.dumps( {
"fields": {
    "description": {
    "content": [
        {
        "content": [
            {
            "text": "My first Jira ticket.",
            "type": "text"
            }
        ],
        "type": "paragraph"
        }
    ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
    "id": "10038"
    },
    "project": {
    "id": "10033"
    },
    "parent": {
    "key": "AR"
    },
    "summary": "First JIRA Ticket",
},
"update": {}
} )

response = requests.request(
"POST",
url,
data=payload,
headers=headers,
auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
