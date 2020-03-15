import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="testdb"
    )
my_cursor = mydb.cursor()

my_sql="DELETE FROM users WHERE user_id = 4"
my_cursor.execute(my_sql)
mydb.commit()

my_sql="DELETE FROM users WHERE name='Tim'"
my_cursor.execute(my_sql)
mydb.commit()
