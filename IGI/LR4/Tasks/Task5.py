"""
Lab №4
Completed by Fyodor Kovalchuck, group 353504.
variant 12
The program presents work with classes, serializers, regular expressions, standard libraries.
v1.0
Development date:
10.05.2025
"""

from .ITask import ITask

from Utils.input import input_float, input_int, input_positive_int

import numpy

from .MatrixOpp import MatrixOperations, MatrixBase
from .MatrixStats import Statistics

class Task5(ITask):
    """
    Class to perform matrix operations including randomization, insertion,
    and statistical calculations.

    Methods:
    - run: Executes the matrix operations and displays the results.
    - _input_values: Prompts the user for the number of rows and columns.
    """
    def run(self):
        """
        Executes the matrix operations:
        1. Inputs the number of rows and columns.
        2. Generates a random matrix.
        3. Inserts the first row after the row containing the minimum element.
        4. Calculates and prints the median using both built-in and custom methods.
        5. Calculates and prints statistical results including mean, median, variance,
           standard deviation, and correlation between the first and last columns.
        
        Raises:
        ValueError: If the number of columns is less than 2.
        Exception: For any unexpected errors during execution.
        """
        try:
            rows, cols = Task5._input_values()
            if cols < 2:
                raise ValueError("Должно быть минимум две колонки для кореляции.")

            matrix = MatrixBase(rows,cols)
            matrix = matrix.randomize(5, 10)

            print("Рандомная матрица:")
            print(matrix)

            MatrixOperations.insert_after_min(matrix)
            print("Матрица после подстановки:")
            print(matrix)

            print("Медиана встроенной функцией:")
            MatrixOperations.find_median_buildin(matrix)

            print("Медиана програмированной функцией:")
            MatrixOperations.find_median_prog(matrix)

            print("\Статистические результаты:")
            print(f"Mean: {Statistics.mean(matrix):.2f}")
            print(f"Median: {Statistics.median(matrix):.2f}")
            print(f"Variance: {Statistics.variance(matrix):.2f}")
            print(f"Standard Deviation: {Statistics.std_dev(matrix):.2f}")
            print(f"Correlation between first and last columns: {Statistics.correlation(matrix, 0, -1)}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


    @staticmethod
    def _input_values():
        """
        Input values:
            - n: The number of rows in the matrix.
            - m: The number of columns in the matrix.

        :return: input values as tuple(n, m).
        """
        n = 0
        m = 0

        while True:
            n = int(input("Введите колво строк: "))
            if n > 0: break
            else: print("Ошибка: введите положительное число!")

        while True:
            m = int(input("Введите колво столбцов: "))
            if m > 0: break
            else: print("Ошибка: введите положительное число!")

        return n, m