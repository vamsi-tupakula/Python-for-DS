from bs4 import BeautifulSoup
import requests

source = requests.get('https://example.com/').text

soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())