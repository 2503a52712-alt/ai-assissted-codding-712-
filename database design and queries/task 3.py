import sqlite3

connection = sqlite3.connect(":memory:")
connection.execute("PRAGMA foreign_keys = ON")
cursor = connection.cursor()

cursor.executescript("""
CREATE TABLE Books (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL
);

CREATE TABLE Members (
    member_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

CREATE TABLE Loans (
    loan_id INTEGER PRIMARY KEY,
    book_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,
    loan_date TEXT NOT NULL,
    returned_date TEXT,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

CREATE INDEX idx_loans_returned_date ON Loans(returned_date);
CREATE INDEX idx_loans_member_id ON Loans(member_id);

INSERT INTO Books (title, author)
VALUES ('Learning SQL', 'Alan Beaulieu'),
       ('Python Basics', 'David Amos'),
       ('Database Design', 'Thomas Connolly');

INSERT INTO Members (name, email)
VALUES ('Asha Kumar', 'asha@example.com'),
       ('Ravi Shah', 'ravi@example.com');

INSERT INTO Loans (book_id, member_id, loan_date, returned_date)
VALUES (1, 1, date('now', '-10 days'), NULL),
       (2, 1, date('now', '-40 days'), NULL),
       (3, 2, date('now', '-50 days'), date('now', '-20 days'));
""")

# Retrieve all books currently issued
cursor.execute("""
    SELECT b.title, m.name AS member, l.loan_date
    FROM Loans AS l
    JOIN Books AS b ON b.book_id = l.book_id
    JOIN Members AS m ON m.member_id = l.member_id
    WHERE l.returned_date IS NULL
    ORDER BY l.loan_date
""")
print("Currently issued books:", cursor.fetchall())

# Find books on loan for more than 30 days
cursor.execute("""
    SELECT b.title, m.name AS member, l.loan_date
    FROM Loans AS l
    JOIN Books AS b ON b.book_id = l.book_id
    JOIN Members AS m ON m.member_id = l.member_id
    WHERE l.returned_date IS NULL
      AND julianday('now') - julianday(l.loan_date) > 30
    ORDER BY l.loan_date
""")
print("Overdue books:", cursor.fetchall())

# Count books loaned by each member
cursor.execute("""
    SELECT m.name, COUNT(l.loan_id) AS books_loaned
    FROM Members AS m
    LEFT JOIN Loans AS l ON l.member_id = m.member_id
    GROUP BY m.member_id, m.name
    ORDER BY m.name
""")
print("Books loaned per member:", cursor.fetchall())

connection.close()