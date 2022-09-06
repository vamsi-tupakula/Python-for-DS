import json
import requests

url = 'http://api.quotable.io/random'
res = requests.get(url)

json_data = res.json()

print(json.dumps(json_data, indent=2))