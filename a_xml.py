# Coursera Chapter 13 - XML & XML Parsing - Graded Assignment

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

sum = 0
url = "http://py4e-data.dr-chuck.net/comments_385264.xml"
print ('Retriving: ', url)
xml = urllib.request.urlopen(url).read()  # make this where the url reads into
x = (xml.decode()) #decodes the file into XML Format
print (type(x)) #Prints String format type
print ('Characters retrieved: ', len(x))
tree = ET.fromstring(x) #Takes XML Formatted string and creates Elemet tree for accessing
count = tree.findall('.//count') # Uses XPath Selector to look through the entire tree for any tag named 'count'
print ('Counts: ', len(count)) # list of strings
for item in count:
    #print (type(item))
    i = int(item.text)
    sum = sum + i
print (sum)
