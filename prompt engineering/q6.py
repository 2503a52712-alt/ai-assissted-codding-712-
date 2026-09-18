# Question 6: Few-Shot Prompting (Even or Odd Classification with Validation)  Prompt Used: "Write a Python program that determines whether a given number is even or odd. You must include proper input validation to handle non-integers. Use these examples for your output:
# Input: 8 -> Output: Even
# Input: 15 -> Output: Odd
# Input: 0 -> Output: Even"  AI-Generated Code:  
def check_even_odd(n):
    try:
        val = float(n)
        if not val.is_integer():
            return "Invalid Input"
        val = int(val)
        if val % 2 == 0:
            return "Even"
        else:
            return "Odd"
    except (ValueError, TypeError):
        return "Invalid Input"
#     Task Analysis:  
# DOCX

# Improvement via Examples: By combining few-shot examples with a direct instruction for validation, the generated code precisely mirrors the required outputs ("Even" or "Odd") while wrapping the logic in a robust try-except block.  
# DOCX

# Testing:

# Negative number: -4 → Even

  
# DOCX

# Non-integer (float): 3.5 → Invalid Input

  
# DOCX

# String: "hello" → Invalid Input

  
# DOCX
