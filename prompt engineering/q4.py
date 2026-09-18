# Question 4: Context-Managed Prompting (Optimized Number Classification)Prompt Used: "Act as a senior software engineer. Write an optimized Python program that classifies a number as prime, composite, or neither. Constraints: 1. Include proper input validation (reject negative numbers, strings, and floats). 2. Optimize the prime-checking logic to run in O(sqrt(n)) time."  AI-Generated Code:  
import math

def classify_number(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        return "Invalid input: Please enter a non-negative integer."

    if n <= 1:
        return "Neither"

    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return "Composite"

    return "Prime"
# Task Analysis:  Validation and Optimization: The context and constraints resulted in production-ready code. It explicitly imports the math module to leverage math.isqrt(), achieving the requested O(sqrt(n)) optimization.  Comparison: Compared to the earlier zero-shot and few-shot strategies, context-managed prompting yields vastly superior reliability. It handles invalid inputs gracefully and applies algorithmic efficiency that the basic prompts lacked