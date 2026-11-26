import sqlite3


def main():
    connection = sqlite3.connect("users.db")

    try:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)

        cursor.execute(
            "INSERT INTO users (username, email) VALUES (?, ?)",
            ("asha", "asha@example.com")
        )
        connection.commit()

        username = input("Enter username to look up: ").strip()

        # Safe: the user input is passed as a parameter, not inserted into SQL.
        cursor.execute(
            "SELECT id, username, email FROM users WHERE username = ?",
            (username,)
        )

        user = cursor.fetchone()

        if user:
            print(f"ID: {user[0]}")
            print(f"Username: {user[1]}")
            print(f"Email: {user[2]}")
        else:
            print("User not found.")

    finally:
        connection.close()


if __name__ == "__main__":
    main()