"""Basic calculator functions for arithmetic operations.

This module provides simple functions for addition, subtraction,
multiplication, and division.
"""


def add(a, b):
    """Add two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.
    """
    return a + b


def subtract(a, b):
    """Subtract one number from another.

    Args:
        a: The number to subtract from.
        b: The number to subtract.

    Returns:
        The difference between a and b.
    """
    return a - b


def multiply(a, b):
    """Multiply two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The product of a and b.
    """
    return a * b


def divide(a, b):
    """Divide one number by another.

    Args:
        a: The number to divide.
        b: The number to divide by.

    Returns:
        The result of dividing a by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
