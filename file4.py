fname = input('Enter the file name: ')
player = input('Enter Player last name: ') # Not perfect.. get columns setup using pandas then go from there for searching by last name for batting - give choice, Batting? Pitching? Fielding? then go to that table
try:
    handle = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
for row in handle:
    if not player in row:
        continue
    print(row)
