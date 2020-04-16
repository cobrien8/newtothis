# read file and split to grab email and total lines starting with from

fname = "mbox-short.txt"
fh = open(fname)
t = fh.split()
print (t[2])
count = 0
for row in fh:
    row = row.split()
    if not row.startswith('From '):
        continue
    f = fh.split()
    count = count + 1
    print (f[2])

print("There were", count, "lines in the file with From as the first word")
