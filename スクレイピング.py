import requests
from bs4 import BeautifulSoup
import re
url = "https://news.yahoo.co.jp/"
r= requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
elems = soup.find_all(href=re.compile("https://news.yahoo.co.jp/pickup/"))
for elems in elems:
    print(elems.contents[0])
    print(elems.attrs['href'])
