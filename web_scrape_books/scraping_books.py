import requests
from bs4 import BeautifulSoup

page = requests.get('https://')
soup = BeautifulSoup(page.content, 'html.parser')