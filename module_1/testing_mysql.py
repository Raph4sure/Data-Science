import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "newpassword",
    database = "testdatabase"
)

mycursor = db.cursor()

# -- mycursor.execute("CREATE DATABASE testdatabase")

# mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)"),
mycursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", ("Rapahel", 19))
db.commit()

mycursor.execute ("SELECT * FROM Person")

for list in mycursor:
    print(list)