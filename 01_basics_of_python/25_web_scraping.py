from bs4 import BeautifulSoup
import requests

source = requests.get('https://example.com/').text

soup = BeautifulSoup(source, 'lxml')
div = soup.find('div')

print('Heading :', div.h1.text)
print('Summary :', div.p.text)
print('Link :', div.select_one(":nth-child(3)").a['href'])