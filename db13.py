import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="testdb"
    )
my_cursor = mydb.cursor()

my_cursor.execute("SELECT * FROM users ORDER BY age DESC")
result= my_cursor.fetchall()
for row in result:
    print(row)
my_cursor.execute("SELECT * FROM users ORDER BY age ASC")
result= my_cursor.fetchall()
for row in result:
    print(row)
