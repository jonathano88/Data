import requests
from bs4 import BeautifulSoup

url = 'URL_OF_THE_PAGE'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')