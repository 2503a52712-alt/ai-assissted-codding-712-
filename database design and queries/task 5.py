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

CREATE TABLE Subjects (
    subject_id INTEGER PRIMARY KEY,
    subject_name TEXT NOT NULL UNIQUE
);

CREATE TABLE Exams (
    exam_id INTEGER PRIMARY KEY,
    subject_id INTEGER NOT NULL,
    exam_date TEXT NOT NULL,
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id)
);

CREATE TABLE Results (
    student_id INTEGER NOT NULL,
    exam_id INTEGER NOT NULL,
    marks REAL NOT NULL CHECK (marks >= 0 AND marks <= 100),
    PRIMARY KEY (student_id, exam_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (exam_id) REFERENCES Exams(exam_id)
);

INSERT INTO Students (name, email)
VALUES ('Asha Kumar', 'asha@example.com'),
       ('Ravi Shah', 'ravi@example.com');

INSERT INTO Subjects (subject_name)
VALUES ('Database Systems'), ('Programming');

INSERT INTO Exams (subject_id, exam_date)
VALUES (1, '2026-04-10'), (2, '2026-04-12');

INSERT INTO Results (student_id, exam_id, marks)
VALUES (1, 1, 88), (1, 2, 92), (2, 1, 76);
""")

# Insert an examination result
cursor.execute("""
    INSERT INTO Results (student_id, exam_id, marks)
    VALUES (?, ?, ?)
""", (2, 2, 81))
connection.commit()

# Retrieve subject-wise marks for a student
student_id = 1
cursor.execute("""
    SELECT s.subject_name, e.exam_date, r.marks
    FROM Results AS r
    JOIN Exams AS e ON e.exam_id = r.exam_id
    JOIN Subjects AS s ON s.subject_id = e.subject_id
    WHERE r.student_id = ?
    ORDER BY s.subject_name
""", (student_id,))
print("Student marks:", cursor.fetchall())

# Calculate average marks for each subject
cursor.execute("""
    SELECT s.subject_name, AVG(r.marks) AS average_marks
    FROM Subjects AS s
    LEFT JOIN Exams AS e ON e.subject_id = s.subject_id
    LEFT JOIN Results AS r ON r.exam_id = e.exam_id
    GROUP BY s.subject_id, s.subject_name
    ORDER BY s.subject_name
""")
print("Subject averages:", cursor.fetchall())

connection.close()