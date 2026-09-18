# Task 3: Runtime Error – File Not Found
# Prompt Given to AI

# “Fix this Python program so that it handles a missing file safely using try-except and gives a user-friendly error message.”

# Buggy Code
def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

print(read_file("nonexistent.txt"))
# Error
# FileNotFoundError: [Errno 2] No such file or directory
# AI-Suggested Solution

# Use a try-except block to handle the FileNotFoundError.

# Corrected Code
def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Error: File not found."
    except OSError:
        return "Error: Invalid file path."


print(read_file("nonexistent.txt"))
# Output for Missing File
# Error: File not found.
# Testing 3 Scenarios
# Scenario 1: File exists
with open("test.txt", "w") as f:
    f.write("Hello AI Debugging")

assert read_file("test.txt") == "Hello AI Debugging"

# Scenario 2: File is missing
assert read_file("missing.txt") == "Error: File not found."

# Scenario 3: Invalid path
assert read_file("invalid/path/file.txt") == "Error: Invalid file path."

print("All 3 test cases passed.")
# Output
# All 3 test cases passed.
# Explanation
#
# The try block attempts to open the file. If the file does not exist, FileNotFoundError is caught and a friendly message is displayed instead of crashing the program.