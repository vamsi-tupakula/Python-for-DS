import json
from textwrap import indent

"""WORKING WITH STRINGS"""

# people_string = '''
# {
#     "people": [
#         {
#             "name": "jack sparrow",
#             "phone": "2939830909",
#             "emails": ["jack@gmail.com", "sparrow@gmail.com"],
#             "has_license": false
#         },
#         {
#             "name": "iron man",
#             "phone": "29399099734",
#             "emails": null,
#             "has_license": true
#         }
#     ]
# }
# '''

# data = json.loads(people_string)
# print(type(data))
# print(type(data['people']))
# print()
# for person in data['people']:
#     del person['emails']

# new_string = json.dumps(data, indent=2, sort_keys=True)
# print(new_string)


"""WORKING WITH JSON FILE"""

with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'], "--", state['abbreviation'])