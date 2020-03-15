import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="testdb"
    )
my_cursor = mydb.cursor()

my_cursor.execute("SELECT * FROM users")
result= my_cursor.fetchall()
for row in result:
    print(row)

my_cursor.execute("SELECT * FROM users")
result= my_cursor.fetchall()
for row in result:
    print(row[0])

my_cursor.execute("SELECT name FROM users")
result= my_cursor.fetchall()
for row in result:
    print(row)
