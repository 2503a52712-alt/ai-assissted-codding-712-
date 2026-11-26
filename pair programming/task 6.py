history = []

def calculate(first, operator, second):
    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    elif operator == "/":
        if second == 0:
            raise ValueError("Cannot divide by zero.")
        result = first / second
    else:
        raise ValueError("Unsupported operator. Use +, -, *, or /.")

    history.append(f"{first} {operator} {second} = {result}")
    return result

while True:
    try:
        first_input = input("Enter the first number (or q to quit): ")
        if first_input.lower() == "q":
            break

        first = float(first_input)
        operator = input("Enter an operator (+, -, *, /): ")
        second = float(input("Enter the second number: "))

        result = calculate(first, operator, second)
        print("Result:", result)

    except ValueError as error:
        print("Error:", error)

print("\nCalculation history:")
for item in history:
    print(item)