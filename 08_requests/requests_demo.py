import requests

url = 'https://xkcd.com/353/'
res = requests.get(url)

# get all the methods and attributes available for res
print(dir(res))