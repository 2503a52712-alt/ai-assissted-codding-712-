# Task 3: AI-Based Code Completion for Class Attributes Validation
# Prompt

# “Generate a Python class User that validates age and email using conditional statements.”

# Python Code
class User:
    def __init__(self, age, email):
        self.age = age
        self.email = email

    def validate(self):
        if self.age >= 18:
            print("Age is valid")
        else:
            print("Age is invalid")

        if "@" in self.email and "." in self.email:
            print("Email is valid")
        else:
            print("Email is invalid")


user = User(20, "student@gmail.com")
user.validate()
# Output
Age is valid
Email is valid
# Test Case 1 – Valid Input
# Age = 20
# Email = student@gmail.com

# Output:

# Age is valid
# Email is valid
# Test Case 2 – Invalid Input
# Age = 15
# Email = studentgmail.com

# Output:

# Age is invalid
# Email is invalid
# Verification
# if self.age >= 18 checks age.
# "@" in self.email checks for @.
# "." in self.email checks for a dot.
# The else statements handle invalid inputs.
# Note: This is a simple educational validation; real applications should use stronger email validation.