# Question 5: Zero-Shot Prompting (Perfect Number Check)Prompt Used: "Write a Python function that checks whether a given number is a perfect number."  AI-Generated Code:  
def is_perfect_number(n):
    if n <= 0:
        return False
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum == n
# Task Analysis:  Testing: Input 28 returns True. Input 12 returns False.  Inefficiencies: Because no constraints were provided (zero-shot), the AI generated a brute-force O(n) solution. Iterating all the way up to n - 1 is highly inefficient for large numbers. The loop should ideally only run up to n // 2 or use a square root optimization.  