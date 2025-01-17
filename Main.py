from bs4 import BeautifulSoup 
import scrapy
import requests
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

# The rent page I am scraping
# https://housinganywhere.com/de/s/Berlin--Deutschland

root_url = 'https://housinganywhere.com'
page_url = root_url + '/de/s/Berlin--Deutschland' 

response = urlopen(page_url)
html = response.read().decode('utf-8')

"""
try:
    response = urlopen(page_url)
    html = response.read().decode('utf-8')
    print(html)
except HTTPError as e:
    print(f"HTTP Error: {e.code}")
except URLError as e:
    print(f"URL Error: {e.reason}")
"""
soup = BeautifulSoup(response, 'html.parser')
# Pretty print the entire HTML
print(soup.prettify())

