import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Priya@1234",
    database="hrms_db"
)

cursor = db.cursor(dictionary=True)
