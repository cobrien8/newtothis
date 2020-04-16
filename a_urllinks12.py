# BeatufiulSoup Assignment - Chapter 12 - Coursera - Parsing HTML Web page data

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

url = 'http://py4e-data.dr-chuck.net/comments_385262.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser') # beautiful soup parses the file - returns an object in SOUP OBJECT
lst = []
# Retrieve all of the anchor tags
tags = soup('tr') # GO through ALL and give me a list of all those tags in tags
#print (soup)
#print (tags)
for tag in tags:
    tag = str(tag)
    t = re.findall('>([0-9]+)',tag)
    if len(t) != 1:
        continue
    if len(t) == 1:
        num = t[0] #take first element (the number) in the list and convert to int
        n = int(num)
        lst.append(n)
        #print (n)
print (sum(lst))
