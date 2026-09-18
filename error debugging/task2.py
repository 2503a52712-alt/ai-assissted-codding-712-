# Task 2: Incorrect Condition in an If Statement
# Prompt Given to AI

# “Find and fix the error in this if statement and explain why it causes a bug.”

# Buggy Code
def check_number(n):
    if n = 10:
        return "Ten"
    else:
        return "Not Ten"
    Error
# SyntaxError: invalid syntax
# AI-Identified Problem

# = is the assignment operator, whereas == is the comparison operator.

# An if condition must use == when checking whether two values are equal.

# Corrected Code
def check_number(n):
    if n == 10:
        return "Ten"
    else:
        return "Not Ten"
    # Sample Output
    print(check_number(10))
print(check_number(5))
Ten
Not Ten
# Assert Test Cases
assert check_number(10) == "Ten"
assert check_number(5) == "Not Ten"
assert check_number(20) == "Not Ten"

print("All 3 test cases passed.")
# Output
# All 3 test cases passed.
# Explanation
# = → assigns a value.
# == → compares two values.

# Therefore, n == 10 is the correct condition..