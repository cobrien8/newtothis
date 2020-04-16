import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_42.json'

uh = urllib.request.urlopen(url)
data = uh.read().decode()
print ('Retrievd',len(data),'characters')

info = json.loads(data)
comments = (info['comments']) #grabs comments, a list of dictionaries
print (len(comments)) # of comments
sum = 0

for item in comments:
    count = item['count']
    count = int(count)
    sum = sum + count

print (sum)
