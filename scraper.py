import requests
from bs4 import BeautifulSoup

# print(requests.get('https://example.com').content)
page = requests.get('https://example.com')
soup = BeautifulSoup( page.content, 'html.parser')
print(soup.find('a'))