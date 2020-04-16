# Parsing web pages (HTML Pages) with beautiful soup


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser') # beautiful soup parses the file - returns an object in Soup object

# Retrieve all of the anchor tags
tags = soup('a') # gives a list of
print (soup)
print (tags)
for tag in tags:
    print (tag.get('href',None)) # Grabs the href line and prints it out
    print (type(tag.get('href',None)))
