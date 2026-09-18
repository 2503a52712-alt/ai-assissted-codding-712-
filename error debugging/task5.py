# Task 5: TypeError – Mixing String and Integer
# Prompt Given to AI

# “Fix this TypeError and provide two solutions: type casting and string concatenation.”

# Buggy Code
def add_five(value):
    return value + 5

print(add_five("10"))
# Error
# TypeError: can only concatenate str (not "int") to str
# Reason

# "10" is a string, while 5 is an integer. Python cannot directly add them.

# Solution 1: Type Casting

# Convert the string into an integer.
def add_five(value):
    return int(value) + 5


print(add_five("10"))
# Output
# 15
# Assert Tests
assert add_five("10") == 15
assert add_five("5") == 10
assert add_five("20") == 25

print("All 3 test cases passed.")
# Output
All 3 test cases passed.
# Solution 2: String Concatenation

# If the intention is to join the values as text, convert 5 into a string.
def add_five(value):
    return value + str(5)


print(add_five("10"))
# Output
105
# Assert Tests
assert add_five("10") == "105"
assert add_five("5") == "55"
assert add_five("20") == "205"

print("All 3 test cases passed.")
# Output
# All 3 test cases passed.
# Comparison
# Method	Code	Result
# Type casting	int(value) + 5	15
# String concatenation	value + str(5)	105

# Type casting should be used when mathematical addition is required.
# String concatenation should be used when the values need to be joined as text.
