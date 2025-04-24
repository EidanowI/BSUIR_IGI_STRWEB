# Task1
# 12
# Kovalchuck Feodor 353504

 
import math
from asin_approx import asin_approx

def run_task1():
    """
    Executes Task 1: Computes arcsin(x) using series approximation.

    This function:
    - Prompts the user for x (|x| <= 1) and precision (eps).
    - Computes arcsin(x) using a series approximation (via ln_approx).
    - Compares the result with the exact value from math.asin.
    - Displays results in a formatted table.
    - Repeats until the user chooses to stop, then returns to the menu.

    Returns:
        None
    
    Notes:
        - Handles invalid input with error messages.
        - Requires the ln_approx function and math module.
    """
    print("Добро пожаловать в программу вычисления arcsin(x) с помощью ряда!")
    while True:
        try:
            x = float(input("Введите x (|x| < 1): "))
            eps = float(input("Введите eps (точность): "))
            approx, n_terms = asin_approx(x, eps)
            if approx is not None:
                math_value = math.asin(x)
                print(f"{'x':<10} {'n':<5} {'F(x)':<15} {'Math F(x)':<15} {'eps':<10}")
                print("-" * 56)
                print(f"{x:<10.5f} {n_terms:<5} {approx:<15.10f} {math_value:<15.10f} {eps:<10.5f}")
        except ValueError:
            print("Ошибка: введите корректные числовые значения")
        again = input("\nАнализировать еще раз? (да/нет): ").strip().lower()
        if again != 'да':
            print("До свидания!")
            return 