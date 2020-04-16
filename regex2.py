# 11.2 Extracting Data - Spam Condifence in emails

import re
hand = open('mbox-short.txt')
lst = ()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('X-DSPAM-Confidence: ([0-9.],+)',line) #starts with finding line and finds floating points
    if len(stuff) != 1: #filter to match 1 floating point number - way to weed out bad lines / data
        continue
    num = float(stuff[0])
    lst.append(num)
print('Maximum:', max(lst))
