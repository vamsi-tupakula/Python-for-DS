import requests

img_url = 'https://imgs.xkcd.com/comics/python.png'
res = requests.get(img_url)

with open('comic.png', 'wb') as f:
    f.write(res.content)