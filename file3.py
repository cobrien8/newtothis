fname = input('Enter the file name: ')
player = input('Enter last name: ') # Not perfect.. get columns setup using pandas then go from there for searching by last name for batting - give choice, Batting? Pitching? Fielding? then go to that table
try:
    handle = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
count = 0
for row in handle:
    if row.startswith(player):
        count = count + 1 #searching for criteria (example uses emails)
        t = row.split(',') #, delimeters
        playerid = t[0]
        print(row)
