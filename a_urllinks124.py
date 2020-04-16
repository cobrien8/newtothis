# BeatufiulSoup Assignment 2 - Chapter 12 - Coursera - Parsing HTML Web page data

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

url = 'http://py4e-data.dr-chuck.net/known_by_Conner.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser') # beautiful soup parses the file - returns an object in Soup object
count = 7 # Can update for # of times you want to crawl thru Urllinks2
pos = 17 # Can update for starting position
tags = soup('a') # list of tags w/ 'a'
lst = []
counts = 0
while counts < count:
    tag = (tags[pos]) #starting point of 2 - get name and Url, go to url and continue
    line = (tag.get('href',None)) # Grabs the href line and prints it out
    n = (re.findall('by_(.+).html',line)) # grabs the name of the person in next search
    name = str(n[0]) #convert name to string
    line = line.split()
    next = str(line[0]) #grabs destination URL address
    lst.append(name) #append name of person from found link to lst
    print (next)
    dest = urllib.request.urlopen(next).read() #Go to destination address from above
    ss = BeautifulSoup(dest, 'html.parser')
    tags = ss('a') # RE-ASSIGN Tags variable here - Code will pick up on the NEW Url and these new tags
    counts = counts + 1
print (lst)
