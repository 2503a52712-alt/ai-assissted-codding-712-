# Task 5: AI-Assisted Code Completion Review
# Prompt

# “Generate a Python program for a simple bank account system using class, loops, and conditional statements.”

# Python Code
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def show_balance(self):
        print("Current Balance:", self.balance)


account = BankAccount("Rahul", 5000)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == 3:
        account.show_balance()

    elif choice == 4:
        print("Thank you for using the bank system.")
        break

    else:
        print("Invalid choice.")
        # Sample Output
        1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 1
Enter deposit amount: 2000
Amount deposited successfully.

1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 3
Current Balance: 7000.0

1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 2
Enter withdrawal amount: 1000
Amount withdrawn successfully.

1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 3
Current Balance: 6000.0

1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 4
# Thank you for using the bank system.
# Strengths of AI-Generated Code
# AI generates code quickly.
# It reduces programming time.
# It provides proper syntax and structure.
# It helps beginners understand programming concepts.
# It can combine classes, loops, and conditional statements effectively.
# It can suggest improvements and alternative solutions.
# Limitations of AI-Generated Code
# AI-generated code may contain logical errors.
# The code should always be tested before use.
# AI may generate unnecessary or inefficient code.
# The programmer may not understand the code if they copy it directly.
# AI-generated code may not handle all unusual input cases.
# Reflection on AI-Assisted Coding

# AI-assisted coding makes programming faster and easier, especially for generating basic code and learning syntax. However, the programmer must understand, test, and verify the generated code instead of blindly copying it.

# AI should be used as a coding assistant, while the final responsibility for correctness, security, and quality remains with the programmer.