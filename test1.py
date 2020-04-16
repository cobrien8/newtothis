import pyodbc
# Some other example server values are
# server = 'localhost\tc' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'CHI-WL-7971\SQLEXPRESS'
database = 'bball'
username = 'TC\\connor.obrien'
password = 'Spreadhope!23'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute('select * from bball.dbo.batting')

for row in cursor:
    print('row = %r' % (row,))
