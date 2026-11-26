# Buggy version (uncomment to see the error)
# numbers = [10, 20, 30]
# total = 0
# for number in numbers:
#     total = number
# print("Average:", total / len(numbers))

# Corrected version
numbers = [10, 20, 30]

if not numbers:
    print("Cannot calculate the average of an empty list.")
else:
    total = sum(numbers)
    average = total / len(numbers)
    print("Average:", average)