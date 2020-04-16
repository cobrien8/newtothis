#Coursera Assmt - 7.2 slicing strings 
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
tot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    pos = line.find(":")
    x = line[pos+1:].lstrip()
    y = float(x)
    count = count + 1
    tot = tot + y
print("Average spam confidence:",tot/ count)
