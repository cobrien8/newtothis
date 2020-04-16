# Regular Expression

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:',line):
        print(line)

# Same as below using Find instead of Reg expression searching
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)

# Case 2 -- Use Startswith Function + using search to match that operation

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

        import re
        hand = open('mbox-short.txt')
        for line in hand:
            line = line.rstrip()
            if re.search('^From:',line): # diff from above is ^ : matches beginning of line - returns true if the line starts with an F, if there is a from somewhere else in the line it will return false
                print(line)
