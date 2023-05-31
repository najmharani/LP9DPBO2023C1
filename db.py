import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_praktikum"
)

dbcursor = mydb.cursor()