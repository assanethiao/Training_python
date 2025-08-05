import sqlite3

conn = sqlite3.connect("mydatabase.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")
cur.executemany("INSERT OR IGNORE INTO users VALUES (?, ?)", [
    (1, "Alice"),
    (2, "Bob"),
    (3, "Charlie")
])
conn.commit()
cur.execute("SELECT * FROM users")

rows = cur.fetchall()
for i in  rows:
    print("ID: " , i[0],  "PRENOM: ", i[1])

conn.close()
