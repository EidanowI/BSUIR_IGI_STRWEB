# TASK2
# 12
# kOVALCHUK FEODOR 353504

import random
from decorator import log_decorator

def input_list():
    """
    Prompts the user to input a list of floating-point numbers.
    
    The function repeatedly asks for input until a valid list is provided.
    It expects numbers separated by spaces and handles invalid inputs gracefully.
    
    Returns:
        list: A list of floating-point numbers entered by the user.
    """
    while True:
        try:
            input_str = input("Введите элементы списка через пробел: ")
            numbers = [float(num) for num in input_str.split()]
            if not numbers:
                print("Список не может быть пустым. Попробуйте снова.")
                continue
            return numbers
        except ValueError:
            print("Ошибка: Введите только вещественные числа, разделённые пробелами.")

def generate_random_list(size, min_val=-10.0, max_val=10.0):
    """
    Generates a list of random floating-point numbers.
    
    Args:
        size (int): The number of elements to generate.
        min_val (float, optional): The minimum value for the random numbers. Defaults to -10.0.
        max_val (float, optional): The maximum value for the random numbers. Defaults to 10.0.
    
    Returns:
        list: A list of random floating-point numbers.
    """
    return [random.uniform(min_val, max_val) for _ in range(size)]

def find_product_of_positive(numbers):
    """
    Calculates the product of all negative numbers in the list.
    
    Args:
        numbers (list): A list of floating-point numbers.
    
    Returns:
        float: The product of all negative numbers. Returns 1 if there are no negative numbers.
    """
    product = 1
    for num in numbers:
        if num >= 0:
            product *= num
    return product

def find_sum_before_min_abs(numbers):
    """
    Calculates the sum of all positive numbers before the element with the maximum absolute value.
    
    Args:
        numbers (list): A list of floating-point numbers.
    
    Returns:
        float: The sum of positive numbers before the element with the maximum absolute value.
               Returns 0 if the list is empty.
    """
    if not numbers:
        return 0
    
    # Находим индекс элемента с минималным модулем
    min_abs_index = min(range(len(numbers)), key=lambda i: abs(numbers[i]))
    
    # Суммируем положительные элементы до этого индекса
    sum_positive = sum(num for num in numbers[:min_abs_index])
    return sum_positive

def print_list(numbers):
    """
    Prints the list to the console.
    
    Args:
        numbers (list): The list to be printed.
    """
    print("Список:", numbers)
    
@log_decorator
def count_in_range(numbers, bound = 12):
    """
    Counts the number of integers bigger then 12.
    
    Args:
        numbers (list): A list of integers.
        bound (int): A bound value
    
    Returns:
        int: The count of numbers bigger then 12.
    """
    count = 0
    for num in numbers:
        if num > bound:
            count += 1
    return count