import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="testdb"
    )
my_cursor = mydb.cursor()

my_cursor.execute("SELECT * FROM users LIMIT 3 OFFSET 1")
result= my_cursor.fetchall()
for row in result:
    print(row)
