#outward in - tables need created first for players. player id table, name player id etc. player id in all tables
#DATA MODEL - start simple

import sqlite3
import re

conn = sqlite3.connect('players.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Players')

cur.execute('''
CREATE TABLE Players (playerid text not null unique, birthyear integer, birthmonth integer, birthday integer,
birthcountry text, birthstate text, birthcity text, deathyear integer, deathmonth integer, deathday integer, deathcountry TEXT,
deathstate text, deathcity text, firstname text, lastname text, givenname text, weight integer, height integer, bats text, throws text,
debut text, finalgame text, retroid text, bbrefid text)''')

fname = 'Master.txt' # Master -- People table - playerid links to ALL other files
fh = open(fname)
for line in fh:
    pieces = line.split(',') # split that line
    #print (pieces)
    playerid = pieces[0]
    birthyear = pieces[1]
    birthmonth = pieces[2]
    birthday = pieces[3]
    birthcountry = pieces[4]
    birthstate = pieces[5]
    birthcity = pieces[6]
    deathyear = pieces[7]     #  RUNNING SLOWLY BECAUSE OF SO MUCH DATA FLOWING INTO THE TABLE AND UNUSED
    deathmonth = pieces[8]
    deathday = pieces[9]
    deathcountry = pieces[10]
    deathstate = pieces[11]
    deathcity = pieces[12]
    firstname = pieces[13]
    lastname = pieces[14]
    givenname = pieces[15]
    weight = pieces[16]
    height = pieces[17]
    bats = pieces[18]
    throws = pieces[19]
    debut = pieces[20]
    finalgame = pieces[21]
    retroid = pieces[22] # retrosheet ID
    bbrefid = pieces[23] # BBALL Ref Website ID used
    #print ((lastname,firstname))

    #Execution below ? - Dangerous to put full text - the ? is a placeholder and avoids a SQL Injection (can google this)
    # the (Email,)) below turns the email field from above into a tuple
    #the below line isnt retrieving any data, just looking at the SQL make sure table name is right and no errors
    #below is opening a record set really - reading it like a file - could have added limit clause for testing

    #cur.execute('SELECT count FROM Players WHERE playerid = ?', (playerid,))

    #Row is going to be record we get back from the datebase
    row = cur.fetchone() #like the GET - if the row isn't there.. then Insert
    if row is None:
        cur.execute('''INSERT INTO Players (playerid, birthyear, birthmonth, birthday, birthcountry, birthstate, birthcity, deathyear, deathmonth, deathday, deathcountry, deathstate,
        deathcity, firstname, lastname, givenname, weight, height, bats, throws, debut, finalgame, retroid, bbrefid)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                ''', (playerid, birthyear, birthmonth, birthday, birthcountry, birthstate, birthcity, deathyear, deathmonth, deathday, deathcountry, deathstate, deathcity, firstname, lastname, givenname, weight, height, bats, throws, debut, finalgame, retroid, bbrefid))
                # set it equal to 1 for count, ? is placeholder for email
                #gives a tuple with the (email,))
    else:
        continue

         #always better to update, other apps can be talking to databse their too
    #using update is way better than reading and adding
        #cur.execute('UPDATE Players SET count = count + 1 WHERE org = ?',
        #            (org,)) #if it exists just add to the count
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT birthmonth, count(playerid) FROM Players group by birthmonth'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
