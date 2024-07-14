import json

data = '''{
    "name" : "Arvind",
    "phone" : {
        "type" : "airtel",
        "number" : "+91 978645312"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name: ', info['name'])
print('Phone no: ',info['phone']['number'])
