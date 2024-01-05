def sum_of_even_numbers(numbers):
    """
    Calculate the sum of all even numbers in a given list.

    Parameters:
    - numbers (list): A list of integers.

    Returns:
    - int: The sum of all even numbers in the list.
    """
    even_sum = 0
    for number in numbers:
        if number % 2 == 0:
            even_sum += number
    return even_sum


# Example usage:
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_even_numbers(numbers_list)
print(f"The sum of even numbers is: {result}")
