import sqlite3

con = sqlite3.connect("student.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")

cur.execute(
    "INSERT OR IGNORE INTO student VALUES (?, ?)",
    (1, "Joy Sen")
)

cur.execute(
    "UPDATE student SET name = ? WHERE id = ?",
    ("Joy Sen", 1)
)

con.commit()

cur.execute("SELECT * FROM student")
print(cur.fetchall())

con.close()