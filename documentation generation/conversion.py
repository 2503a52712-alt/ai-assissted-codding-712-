"""Simple functions for converting numbers between common bases."""


def decimal_to_binary(n):
    """Convert a decimal integer to a binary string.

    Args:
        n (int): The decimal integer to convert.

    Returns:
        str: The binary representation of n without a ``0b`` prefix.
    """
    return format(n, "b")


def binary_to_decimal(b):
    """Convert a binary string to a decimal integer.

    Args:
        b (str): A non-empty string containing only ``0`` and ``1``.

    Returns:
        int: The decimal value represented by b.

    Raises:
        ValueError: If b is empty or contains characters other than ``0`` and
            ``1``.
        TypeError: If b is not a string.
    """
    if not isinstance(b, str):
        raise TypeError("Binary input must be a string.")
    if b == "" or any(character not in "01" for character in b):
        raise ValueError("Binary input must contain only 0 and 1.")
    return int(b, 2)


def decimal_to_hexadecimal(n):
    """Convert a decimal integer to a hexadecimal string.

    Args:
        n (int): The decimal integer to convert.

    Returns:
        str: The uppercase hexadecimal representation of n without a ``0x``
            prefix.
    """
    return format(n, "X")
