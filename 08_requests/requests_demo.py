import requests

# url = 'https://xkcd.com/353/'
# res = requests.get(url)

# get all the methods and attributes available for res
# print(dir(res))

# get complete page content
# print(res.text)

# get status_code
# print(res.status_code)
# print(res.ok)

# passing parameters into url

payload = {'page': 2, 'count': 20}
res = requests.get('https://httpbin.org/get', params=payload)

print(res.text)
print(res.url)