"""
Lab №4
Completed by Fyodor Kovalchuck, group 353504.
variant 12
The program presents work with classes, serializers, regular expressions, standard libraries.
v1.0
Development date:
10.05.2025
"""

from Utils.input import input_float, input_int, input_positive_int

from .ITask import ITask


import math, statistics, matplotlib.pyplot as plot

class Task3(ITask):
    """
    A class that computes the arcsine of a value using a custom implementation
    and compares it with Python's built-in function. It also generates statistical
    metrics and a plot of the results.

    Attributes:
    - _filepath (str): The path to save the plot image.

    Methods:
    - __init__(filepath: str): Initializes the Task3 instance with the file path.
    - run(): Prompts the user for input, computes arcsine, and displays statistics.
    """
    def __init__(self, filepath: str):
        """
        Initializes the Task3 instance.

        Parameters:
        - filepath (str): The path to save the plot image.
        """
        self._filepath = filepath

    def run(self):
        """
        Executes the arcsine calculation and statistical analysis.

        Prompts the user for a value of x (where |x| < 1) and the precision (eps) 
        for calculations. Computes the arcsine using a custom implementation 
        (`my_asin`) and compares it with the built-in `math.asin` function. 
        Displays various statistical metrics on the computed elements and 
        generates a plot of the arcsine function.
        """
        print("Введите значение аргумента x (|x| < 1): ")
        while True: 
            x = input_float()
            if abs(x) <  1: break
            else: print("Ошибка: |x| < 1")

        print("Введите точность вычислений eps: ")
        eps = input_positive_int()
    
        my_f, elems = my_asin(x, eps)
        math_f = math.asin(x)
        print("Результат работы ручной функции:     ", my_f)
        print("Результат работы встроенной функции: ", math_f)
        print("Среднее арифм. элементов: ", statistics.mean(elems))
        print("Медиана элементов: ", statistics.median(elems))
        print("Мода элементов: ", statistics.mode(elems))
        print("Дисперсия элементов: ", statistics.variance(elems))
        print("Стандартное отклонение: ", statistics.stdev(elems))
        my_asin_plot(eps, self._filepath + 'graph.png')


def my_asin(x, eps, max_iter = 500):
    """
    Calculates arcsine using a Taylor series expansion.

    Parameters:
    - x (float): The value for which to compute the arcsine (|x| < 1).
    - eps (int): The precision of the calculation (number of terms).
    - max_iter (int): Maximum number of iterations (default is 500).

    Returns:
    - asin (float): The computed arcsine of x.
    - elems (list): A list of elements added to the arcsine approximation.
    """
    asin = 0.0
    n = 0
    elems = list()
    if eps > max_iter:
        print("max eps = 500")

    while n <= max_iter:
        if n == eps:
            break
        temp = (math.factorial(2*n) / ((4**n) * (math.factorial(n)**2) * (2*n + 1))) * (x**(2*n + 1))
        elems.append(temp)
        asin += temp
        n += 1
    return asin, elems

def my_asin_plot(n, file_name): 
    """
    Plots the arcsine function computed by the custom implementation and compares 
    it with the built-in math.asin function.

    Parameters:
    - n (int): The precision of the calculation.
    - file_name (str): The filename to save the plot image.
    """
    func = list()
    args = list()
    func_math = list()
    print("--------------------------------")
    print("-x-------n-----F(x)-----MF(x)---")

    for i in range(-10, 11, 1):
        if i / 10 == 1 or i / 10 == -1:
            continue
        y, _ = my_asin(i / 10, n)
        func.append(y)
        y_math = math.asin(i / 10)
        func_math.append(y_math)
        args.append(i / 10)
        print(f"{(i / 10):<6}  {n}  {y:<8.4f}   {y_math:<8.4f}")

    print("--------------------------------")

    plot.axhline(0, color='black',linewidth=0.5)
    plot.axvline(0, color='black',linewidth=0.5)
    plot.xlim(-1, 1)
    plot.ylim(-math.pi/2, math.pi/2)
    plot.plot(args, func, color = 'red')
    plot.plot(args, func_math, color = 'blue')
    plot.title("ASIN")
    plot.ylabel("Ось Y")
    plot.xlabel("Ось X")
    plot.legend(loc = 'lower center', title = 'Красный - пользовательская ф.\n Синий - встроенная ф.')
    plot.annotate(' (0, 0)',
             xy=(0, 0), xycoords='data',
             xytext=(-20, 20), textcoords='offset points',)
    
    plot.savefig(file_name, dpi=300)
    plot.show()