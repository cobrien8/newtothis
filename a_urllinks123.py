import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser') # beautiful soup parses the file - returns an object in Soup object

tags = soup('a')

for tag in tags:
    print(tag.get('href', None))
