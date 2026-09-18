# Task 1: Syntax Error – Missing Parenthesis in Print Statement
# Prompt Given to AI

# “Find and fix the syntax error in this Python code and explain the error.”

# Buggy Code
def greet():
    print("Hello, AI Debugging Lab!"

greet()
# Error
# SyntaxError: '(' was never closed
# AI-Identified Problem

# The print() statement is missing a closing parenthesis ).

# Corrected Code
def greet():
    print("Hello, AI Debugging Lab!")

greet()
# Output
Hello, AI Debugging Lab!
# Assert Test Cases
def greet():
    return "Hello, AI Debugging Lab!"

assert greet() == "Hello, AI Debugging Lab!"
assert isinstance(greet(), str)
assert len(greet()) > 0

print(greet())
print("All 3 test cases passed.")
# Output
Hello, AI Debugging Lab!
All 3 test cases passed.
# Explanation

# The error was caused by a missing ) in the print() statement. After adding it, the program executes correctly.