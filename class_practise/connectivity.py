import sqlite3

# 1. Connect to database
conn = sqlite3.connect("student.db")

# 2. Create cursor
cursor = conn.cursor()

# 3. Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

# 4. Insert data
cursor.execute("""
INSERT INTO students (name, age, course)
VALUES (?, ?, ?)
""", ("Asmit", 19, "CSE AI/ML"))

# 5. Save changes
conn.commit()

# 6. Display data
cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

for row in rows:
    print(row)

# 7. Close connection
conn.close()