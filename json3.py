#Coursera Assignment Ch. 13 - JSON, URL, SOA etc. Connor O'Brien

import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_385265.json'

uh = urllib.request.urlopen(url)
data = uh.read().decode()
print ('Retrievd',len(data),'characters') # Number of characters retrieved in json string

info = json.loads(data)
comments = (info['comments']) #grabs comments, a list of dictionaries
print (len(comments)) # of comments
sum = 0

for item in comments:
    count = item['count']
    count = int(count)
    sum = sum + count

print (sum)
