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

import matplotlib.pyplot as plot
from abc import ABC, abstractmethod
import math

class GeometricFigure(ABC):
    """
    An abstract base class for geometric figures.

    Methods:
    - calculate_area(): Abstract method that must be implemented by subclasses to calculate the area of the figure.
    """
    @abstractmethod
    def calculate_area(self):
        pass

class FigureColor:
    """
    A class to represent the color of a figure using RGB values.

    Attributes:
    - red (int): The red component of the color (0-255).
    - green (int): The green component of the color (0-255).
    - blue (int): The blue component of the color (0-255).

    Methods:
    - __init__(red, green, blue): Initializes the color with specified RGB values.
    """
    def __init__(self, red, green, blue):
        """
        Initializes the FigureColor instance.

        Parameters:
        - red (int): The red component of the color.
        - green (int): The green component of the color.
        - blue (int): The blue component of the color.
        """
        self.red = red
        self.green = green
        self.blue = blue

class Triangle(GeometricFigure):
    """
    A class representing a triangle.

    Inherits from GeometricFigure and implements area calculation.

    Attributes:
    - height (float): The height of the triangle.
    - base (float): The base length of the triangle.
    - color (FigureColor): The color of the triangle.

    Methods:
    - __init__(height, base, red, green, blue): Initializes the triangle with dimensions and color.
    - calculate_area(): Calculates the area of the triangle.
    - info(): Prints information about the triangle.
    - draw(): Draws the triangle using matplotlib.
    - save(file_name): Saves the drawn triangle plot to a file.
    """
    side = 0
    def __init__(self, height, base, red, green, blue):
        """
        Initializes the Triangle instance.

        Parameters:
        - height (float): The height of the triangle.
        - base (float): The base length of the triangle.
        - red (int): Red component of the triangle color.
        - green (int): Green component of the triangle color.
        - blue (int): Blue component of the triangle color.
        """
        super().__init__
        self.height = height
        self.base = base
        self.color = FigureColor(red, green, blue)
    
    @property
    def side(self):
        """
        Calculates the length of the side of the triangle.

        Returns:
        float: The length of the side calculated using the Pythagorean theorem.
        """
        return math.sqrt(self.height**2 + (self.base / 2)**2)

    @side.setter
    def side(self, value):
        self.side = value

    def calculate_area(self):
        """
        Calculates the area of the triangle.

        Returns:
        float: The area of the triangle.
        """
        return 0.5 * self.base * self.height
    
    def info(self):
        """
        Prints information about the triangle, including its color, dimensions, and area.
        """
        if self.color.blue == 255: col_name = 'синий'
        elif self.color.green == 255: col_name = 'зеленый'
        elif self.color.red == 255: col_name = 'красный'
        area = self.calculate_area()
        print("Треугольник: цвет - {0}, высота - {1}, основание - {2}, площадь - {3}".format(col_name, self.height, self.base, area))
    
    def draw(self):
        """
        Draws the triangle using matplotlib.
        """
        figure, ax = plot.subplots()
        triangle = plot.Polygon([[0, 0], [self.base, 0], [self.base/2, self.height]],
                           closed=True,
                           facecolor=(self.color.red/255, self.color.green/255, self.color.blue/255))
        
        ax.add_patch(triangle)
        ax.set_xlim(0, self.base)
        ax.set_ylim(0, self.height)
        plot.title("РАВНОБЕДРЕННЫЙ ТРЕУГОЛЬНИК")
        plot.show()
    def save(self, file_name):
        """
        Saves the drawn triangle plot to a file.

        Parameters:
        - file_name (str): The filename to save the plot image.
        """
        plot.savefig(file_name, dpi=300)

class Task4(ITask):
    
    def __init__(self, filepath: str):

        self._filepath = filepath
    def run(self):

        print("Для измерений треугольника введите:")
        print("Длина основания: ")
        base_len = input_positive_int()
        print("Длина высоты: ")
        height_len = input_positive_int()
        col_type = 0
        while col_type < 1 or col_type > 3:
            print("Введите цвет: 1 - красный, 2 - зеленый, 3 - синий: ")
            col_type = input_positive_int()
        if col_type == 1: red_c, green_c, blue_c = 255, 0, 0
        elif col_type == 2: red_c, green_c, blue_c = 0, 255, 0
        elif col_type == 3: red_c, green_c, blue_c = 0, 0, 255

        triangle = Triangle(height_len, base_len, red_c, green_c, blue_c)
        triangle.info()
        print("Сторона треугольника: ", triangle.side)
        triangle.draw()

        triangle.save(self._filepath + '/triangle.png')