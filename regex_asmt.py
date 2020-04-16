#Chapter 11 Assignment -- Coursera

#Extract numbers from text file and sum all numbers as integers

import re
hand = open('regex_sum_42.txt') #example data set with total of (There are 90 values with a sum=445833)
lst = []

for line in hand:
    line = line.rstrip()
    stuff = re.findall('([0-9]+)',line) #starts with finding line and finds digits in range
    if len(stuff) > 1: #filter to match more than 1 match
        #print ('More than 1!') #finding multiple lines
        for x in stuff: #splitting multi - match line lists into own list
            m = x.split()
            #s = x.split(' ')
            #print (m)
            num = m[0]
            n = int(num) #convert to integers
            print(n)
            lst.append(n)
    #print (stuff)
    if len(stuff) == 1: #filter to match single line matches
        try:
            h = (stuff[0])
            b = int(h)
            lst.append(b)
        except:
            continue
    #print (n)
    #sum = sum + b
print (sum(lst))
