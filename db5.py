import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="testdb"
    )
my_cursor = mydb.cursor()

sqlstuff= "INSERT INTO users(name,email,age) VALUES(%s,%s,%s)"
records=[
    ("Tim","tim@tim.com",32),
    ("Mary","mary@mary.com",21),
    ("Steve","steve@steve.com",25),
    ("Tina","tina@tina.com",31),
    ("Cook","cook@cook.com",23)
]
my_cursor.executemany(sqlstuff,records)
mydb.commit()
