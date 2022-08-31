import json

people_string = '''
{
    "people": [
        {
            "name": "jack sparrow",
            "phone": "2939830909",
            "emails": ["jack@gmail.com", "sparrow@gmail.com"],
            "has_license": false
        },
        {
            "name": "iron man",
            "phone": "29399099734",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

data = json.loads(people_string)
print(type(data))
print(type(data['people']))
print()
for person in data['people']:
    print(person)