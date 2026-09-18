# Task 4: AI-Based Code Completion for Classes
# Prompt

# “Generate a Python class Student with attributes (name, roll number, marks) and methods to calculate total and average marks.”

# Python Code
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)


student = Student("Rahul", 101, [80, 75, 90])

print("Name:", student.name)
print("Roll Number:", student.roll_number)
print("Total Marks:", student.calculate_total())
print("Average Marks:", student.calculate_average())
# Output
Name: Rahul
Roll Number: 101
Total Marks: 245
Average Marks: 81.66666666666667
Verification

# Marks:

# 80 + 75 + 90 = 245

# Average:

# 245 / 3 = 81.67

# Therefore, the program is correct.

# Class Structure
# Class: Student
# Attributes: name, roll_number, marks
# Method 1: calculate_total()
# Method 2: calculate_average()
# Object: student
# Minor Manual Improvement

# The average can be displayed neatly using:
print("Average Marks:", round(student.calculate_average(), 2))

# Output:

Average Marks: 81.67

# Justification: Rounding makes the output more readable.