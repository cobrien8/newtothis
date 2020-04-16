largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        f = float(num)
    except:
        print ('Invalid input')
        continue
    if largest is None or largest < f:
        largest = int(f)
    if smallest is None or smallest > f:
        smallest = int(f)

print("Maximum is", largest)
print("Minimum is", smallest)
