import pyodbc
#import pandas as pd

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=CHI-WL-7971\\SQLEXPRESS;'
                      'Database=bball;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute('SELECT count(bball.dbo.batting.playerID) FROM bball.dbo.batting') #SQL Select Statement
for row in cursor:

    print(row)
