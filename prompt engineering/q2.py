# Question 2: One-Shot Prompting (Factorial Calculation)Prompt Used: "Write a Python function to compute the factorial of a given number.
# Example: Input: 5 -> Output: 120"  AI-Generated Code:  
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
# Task Analysis:  Comparison with Zero-Shot: Providing a single example helps anchor the AI to the exact expected mathematical behavior. The generated code is clear, uses a highly readable iterative approach, and avoids unnecessary complexity (like deep recursion limits).  Clarity and Correctness: The code is perfectly correct for positive integers and zero. However, it still lacks handling for negative inputs (which mathematically do not have a defined factorial in standard contexts), showing that one-shot prompting improves I/O mapping but doesn't automatically generate full edge-case validation.  