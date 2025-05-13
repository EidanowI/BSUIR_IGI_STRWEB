"""
Lab №4
Completed by Fyodor Kovalchuck, group 353504.
variant 12
The program presents work with classes, serializers, regular expressions, standard libraries.
v1.0
Development date:
10.05.2025
"""


def input_int():
    """
    Prompts the user to input an integer.

    This function continuously prompts the user until a valid integer is entered.
    If the input is not a valid integer, it prints an error message and prompts again.

    Returns:
    int: The integer value entered by the user.
    """
    while True:
        try:
            int_num = int(input())
            return int_num
        except ValueError:
            print("Ошибка ввода: введите целое число!")
            continue


def input_float():
    """
    Prompts the user to input a float.

    This function continuously prompts the user until a valid float is entered.
    If the input is not a valid float, it prints an error message and prompts again.

    Returns:
    float: The float value entered by the user.
    """
    while True:
        try:
            float_num = float(input())
            return float_num
        except ValueError:
            print("Ошибка ввода: введите вещественное число!")
            continue
    
def input_positive_int():
    """
    Prompts the user to input a positive integer.

    This function uses the input_int() function to get an integer from the user.
    It continues to prompt until a positive integer is entered. If the input
    is not a positive integer, it prints an error message and prompts again.

    Returns:
    int: The positive integer value entered by the user.
    """
    while True:
        num = input_int()
        if num > 0: return num
        else: print("Ошибка: введите положительное число!")