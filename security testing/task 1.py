import hashlib
import hmac
import re
import secrets
from getpass import getpass

# Demo account. In a real application, store the salt and hash securely.
USERNAME = "student01"
SALT = secrets.token_bytes(16)
PASSWORD_HASH = hashlib.scrypt(
    b"LabPass123!",
    salt=SALT,
    n=2**14,
    r=8,
    p=1
)

USERNAME_PATTERN = re.compile(r"^[A-Za-z0-9_]{3,20}$")


def valid_username(username: str) -> bool:
    return bool(USERNAME_PATTERN.fullmatch(username))


def valid_password(password: str) -> bool:
    return (
        len(password) >= 10
        and any(char.islower() for char in password)
        and any(char.isupper() for char in password)
        and any(char.isdigit() for char in password)
    )


def login(username: str, password: str) -> bool:
    if not valid_username(username) or not valid_password(password):
        return False

    candidate_hash = hashlib.scrypt(
        password.encode("utf-8"),
        salt=SALT,
        n=2**14,
        r=8,
        p=1
    )

    return username == USERNAME and hmac.compare_digest(
        candidate_hash, PASSWORD_HASH
    )


entered_username = input("Username: ").strip()
entered_password = getpass("Password: ")

if login(entered_username, entered_password):
    print("Login successful.")
else:
    print("Invalid username or password.")