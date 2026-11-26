import sqlite3

connection = sqlite3.connect(":memory:")
connection.execute("PRAGMA foreign_keys = ON")
cursor = connection.cursor()

cursor.executescript("""
CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

CREATE TABLE Courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL UNIQUE
);

CREATE TABLE Enrollments (
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    enrollment_date TEXT NOT NULL DEFAULT (date('now')),
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

INSERT INTO Students (name, email)
VALUES ('Asha Kumar', 'asha@example.com');

INSERT INTO Courses (course_name)
VALUES ('Database Systems'), ('Python Programming');

INSERT INTO Enrollments (student_id, course_id)
VALUES (1, 1), (1, 2);
""")

# Insert a new student
cursor.execute(
    "INSERT INTO Students (name, email) VALUES (?, ?)",
    ("Ravi Shah", "ravi@example.com")
)

# Fetch all courses enrolled by a student
student_id = 1
cursor.execute("""
    SELECT c.course_id, c.course_name
    FROM Courses AS c
    JOIN Enrollments AS e ON e.course_id = c.course_id
    WHERE e.student_id = ?
    ORDER BY c.course_name
""", (student_id,))
print("Courses for student:", cursor.fetchall())

# Count students in each course
cursor.execute("""
    SELECT c.course_name, COUNT(e.student_id) AS student_count
    FROM Courses AS c
    LEFT JOIN Enrollments AS e ON e.course_id = c.course_id
    GROUP BY c.course_id, c.course_name
    ORDER BY c.course_name
""")
print("Students per course:", cursor.fetchall())

connection.close()