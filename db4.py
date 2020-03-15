import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="testdb"
    )
my_cursor = mydb.cursor()

sqlstuff= "INSERT INTO users(name,email,age) VALUES(%s,%s,%s)"
record1=("John", "John@academy.com", 40)
my_cursor.execute(sqlstuff , record1)
mydb.commit()
