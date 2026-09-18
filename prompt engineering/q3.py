# Question 3: Few-Shot Prompting (Armstrong Number Check)Prompt Used: "Write a Python function to check whether a given number is an Armstrong number. Use the following examples to guide your output format:
# Input: 153 -> Output: Armstrong Number
# Input: 370 -> Output: Armstrong Number
# Input: 123 -> Output: Not an Armstrong Number"  AI-Generated Code:  
def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)

    if total == n:
        return "Armstrong Number"
    else:
        return "Not an Armstrong Number"
    # Task Analysis:  Influence on Code Structure: The few-shot examples effectively forced the AI to return specific string outputs ("Armstrong Number" and "Not an Armstrong Number") rather than standard boolean (True/False) values.  Testing: Boundary value 0 outputs "Armstrong Number" (which is correct). However, passing an invalid input like a string (e.g., "abc") results in a ValueError, meaning explicit validation logic is still needed