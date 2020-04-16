# 9.4 Dictionaries Assignment! Loop through a file to get the desired email list, count up # of occurences of the email and the email + count in a dictionary

name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    if not line.startswith('From '): # from the lines starting with from, split and give me the email
        continue
    lines = line.split()
    emails = (lines[1])
    counts[emails] = counts.get(emails,0) + 1

bigemail = None
bigcount = None

for k,v in counts.items():
    if bigcount is None or v > bigcount:
        bigemail = k
        bigcount = v

print (bigemail,bigcount)
