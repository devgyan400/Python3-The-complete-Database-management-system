import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="testdb"
    )
my_cursor = mydb.cursor()

my_sql= "DROP TABLE IF EXISTS users"
my_cursor.execute(my_sql)
