def calculate_square(number):
    """
    Calculate the square of a given number.

    Parameters:
    - number (float or int): The number for which the square will be calculated.

    Returns:
    - float or int: The square of the input number.
    """
    square = number ** 2
    return square


# Example usage:
result = calculate_square(5)
print(f"The square of 5 is: {result}")
