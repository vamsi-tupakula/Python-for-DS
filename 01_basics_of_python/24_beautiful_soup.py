from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())
match = soup.title
match_text = soup.title.text
print(match)
print(match_text)

match = soup.find('div', class_='footer')
print(match)
# get h1 tag inside the footer div
print(match.h1.text)