# Task 2: AI-Based Code Completion for Loop with Conditionals
# Prompt

# “Generate Python code to count how many numbers in a list are even and odd.”

# Python Code
numbers = [10, 15, 22, 7, 8, 13]

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)
# Output
Even numbers: 3
Odd numbers: 3
# Logic Flow
# Start
#   ↓
# Take each number from list
#   ↓
# Is number divisible by 2?
#   ↓
# Yes → Increase even count
#   ↓
# No → Increase odd count
#   ↓
# Repeat until list ends
#   ↓
# Display counts
# Correctness Validation

# List:

# 10, 15, 22, 7, 8, 13

# Even numbers = 10, 22, 8 → 3

# Odd numbers = 15, 7, 13 → 3

# Therefore, the result is correct.