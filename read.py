import sqlite3

conn = sqlite3.connect("results.db")
c = conn.cursor()

for row in c.execute("SELECT * FROM results"):
    print(row)

conn.close()