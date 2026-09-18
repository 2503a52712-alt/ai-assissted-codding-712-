# Task 1: AI-Based Code Completion for Loops
# Prompt

# “Generate Python code to print all even numbers between 1 and N using a loop.”

# Python Code
n = int(input("Enter N: "))

print("Even numbers:")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")
        n = int(input("Enter N: "))
# Sample Output
Enter N: 10
Even numbers:
2 4 6 8 10
# Loop Type Used

# for loop

# Logic
# Take the value of N.
# The for loop checks numbers from 1 to N.
# i % 2 == 0 checks whether the number is even.
# If true, the number is printed.
# Validation

# For N = 10, output is:

# 2 4 6 8 10