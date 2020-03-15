import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="testdb"
    )
my_cursor = mydb.cursor()

my_sql = "UPDATE users SET age = 34 WHERE name='Steve'"
my_cursor.execute(my_sql)
mydb.commit()
