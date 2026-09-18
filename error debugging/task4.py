# Task 4: Calling a Non-Existent Method
# Prompt Given to AI

# “Debug this Python class where a non-existent method is called. Decide whether to define the missing method or correct the method call.”

# Buggy Code
class Car:
    def start(self):
        return "Car started"

my_car = Car()
print(my_car.drive())
# Error
# AttributeError: 'Car' object has no attribute 'drive'
# AI-Identified Problem

# The class contains a start() method, but the program tries to call drive(), which is not defined.

# Since the intended operation can be satisfied by the existing start() method, the method call should be corrected.

# Corrected Code
class Car:
    def start(self):
        return "Car started"


my_car = Car()
print(my_car.start())
# Output
# Car started
# Assert Test Cases
class Car:
    def start(self):
        return "Car started"


my_car = Car()

assert my_car.start() == "Car started"
assert isinstance(my_car.start(), str)
assert len(my_car.start()) > 0

print(my_car.start())
print("All 3 test cases passed.")
# Output
# Car started
# All 3 test cases passed.
# Explanation

# drive() does not exist in the Car class. The correct existing method is start(), so the call was changed from:

# my_car.drive()

# to:

# my_car.start()