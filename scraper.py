import requests
from bs4 import BeautifulSoup

# print(requests.get('https://example.com').content)
URL = "https://realpython.github.io/fake-jobs/" # Change this var called URL if you want to scrape a different website. Make sure the scraping though doesn't 
# violate the website's TOS. Also, you can't omit the http://
page = requests.get(URL)
soup = BeautifulSoup( page.content, 'html.parser')
# print(soup.find('h1'))
job_titles = soup.find_all (class_='h2')
# print(soup.title.get_text())
# result = soup.find_all(class_='is-5') You will need to look at the website's code and figure out the HTML class names to scrape the data you need.
# BS (Beautiful Soup) has a find_all method where it locates all data with that class or id tag. 
print(job_titles)