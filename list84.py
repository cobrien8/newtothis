fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for row in fh:
    words = row.split()
    for x in words:
        if x in lst:
            continue
        else:
            lst.append(x)
    lst.sort()
print(lst)
