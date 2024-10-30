import requests
from bs4 import BeautifulSoup
import re

url = "https://ja.m.wikipedia.org"
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
print(soup)
