import sqlite3
db = sqlite3.connect('mydatabase.db')
cursor = db.cursor()
cursor.execute("insert into student_table (name,age) values (?,?)", ('Alice', 24))