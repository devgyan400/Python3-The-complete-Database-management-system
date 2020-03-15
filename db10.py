import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="testdb"
    )
my_cursor = mydb.cursor()

my_cursor.execute("SELECT * FROM users WHERE name LIKE '%a%' AND age= 31")
result= my_cursor.fetchall()
for row in result:
    print(row)

my_cursor.execute("SELECT * FROM users WHERE name LIKE '%a%' OR age= 31")
result= my_cursor.fetchall()
for row in result:
    print(row)

my_cursor.execute("SELECT * FROM users WHERE name LIKE '%a%' AnD age= 31 AND user_id=4")
result= my_cursor.fetchall()
for row in result:
    print(row)
