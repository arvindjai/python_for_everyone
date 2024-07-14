import json

input = '''[
    {   "id" : "1000",
        "user": "root",
        "server" : "ubuntu"
    },
    {   "id" : "1005",
        "user": "admin",
        "server" : "RHEL-9"
    },
    {   "id" : "1020",
        "user": "vindy",
        "server" : "RHEL-7"
    }
]'''

info = json.loads(input)
print(len(info))
for item in info:
    print("UserName: ", item['user'])
    print("ID: ", item['id'])
    print("server: ",item['server'])