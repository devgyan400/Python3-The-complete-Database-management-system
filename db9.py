import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="testdb"
    )
my_cursor = mydb.cursor()

my_cursor.execute("SELECT * FROM users WHERE age>30")
result= my_cursor.fetchall()
for row in result:
    print(row)

my_cursor.execute("SELECT * FROM users WHERE name='Tim'")
result= my_cursor.fetchall()
for row in result:
    print(row)

my_cursor.execute("SELECT * FROM users WHERE name LIKE 'T%'")
result= my_cursor.fetchall()
for row in result:
    print(row)

my_cursor.execute("SELECT * FROM users WHERE name LIKE '%a%'")
result= my_cursor.fetchall()
for row in result:
    print(row)
