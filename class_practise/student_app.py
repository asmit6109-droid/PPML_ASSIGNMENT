import tkinter as tk
from tkinter import messagebox
import sqlite3


# ---------------- DATABASE ----------------

# Connect to SQLite database
conn = sqlite3.connect("student.db")

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
""")

conn.commit()


# ---------------- FUNCTIONS ----------------

def add_student():
    name = name_entry.get()
    age = age_entry.get()
    course = course_entry.get()

    if name == "" or age == "" or course == "":
        messagebox.showwarning("Warning", "Please fill all fields.")
        return

    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )

    conn.commit()

    messagebox.showinfo("Success", "Student added successfully!")

    # Clear input boxes
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)


def show_students():
    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    result_text.delete("1.0", tk.END)

    for student in students:
        result_text.insert(tk.END, str(student) + "\n")


# ---------------- GUI ----------------

root = tk.Tk()

root.title("Student Management System")
root.geometry("500x600")


# Name
name_label = tk.Label(root, text="Name")
name_label.pack(pady=5)

name_entry = tk.Entry(root, width=30)
name_entry.pack()


# Age
age_label = tk.Label(root, text="Age")
age_label.pack(pady=5)

age_entry = tk.Entry(root, width=30)
age_entry.pack()


# Course
course_label = tk.Label(root, text="Course")
course_label.pack(pady=7)

course_entry = tk.Entry(root, width=45)
course_entry.pack()


# Add button
add_button = tk.Button(
    root,
    text="Add Student",
    command=add_student
)

add_button.pack(pady=20)


# Show button
show_button = tk.Button(
    root,
    text="Show Students",
    command=show_students
)

show_button.pack()


# Display area
result_text = tk.Text(root, height=15, width=60)
result_text.pack(pady=20)


# Start application
root.mainloop()


# Close database when program ends
conn.close()  