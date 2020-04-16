# 10.2 Exercise - order email count by time of day it was Statement

name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    if not line.startswith('From '):
        continue
    lines = line.split()
    date = (lines[5])
    pos = date.find(':')
    hour = (date[0:pos])
    counts[hour] = counts.get(hour,0)+1

for k,v in sorted(counts.items()):
    print (k,v)
