import numpy as np

class MatrixBase:
    """Base class for matrix operations."""
    _default_low = 0  # Static attribute for default range
    _default_high = 100

    def __init__(self, rows, cols):
        """Initialize matrix dimensions."""
        self.rows = rows
        self.cols = cols
        self.matrix = None

    @property
    def matrix(self):
        """Get the matrix."""
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        """Set the matrix."""
        self._matrix = value

    def __str__(self):
        """String representation of the matrix."""
        return str(self.matrix)
    
class MatrixRandomizerMixin:
    """Mixin for random matrix generation."""
    def randomize(self, low=None, high=None):
        """Generate a random matrix."""
        low = low if low is not None else MatrixBase._default_low
        high = high if high is not None else MatrixBase._default_high
        return np.random.randint(low, high, size=(self.rows, self.cols))
    
class MatrixOperations(MatrixBase, MatrixRandomizerMixin):
    """Class for matrix operations with NumPy."""
    def __init__(self, rows, cols):
        """Initialize with dimensions and create a random matrix."""
        super().__init__(rows, cols)
        self.matrix = self.randomize()

    def insert_after_min(self):
        """
        Inserts the first row of the matrix immediately after the row containing the minimum element.

        Parameters:
        matrix (np.ndarray): A 2D NumPy array.

        Returns:
        np.ndarray: The modified matrix after insertion.
        """
        min_index = np.argmin(self.matrix)
        min_row, min_col = np.unravel_index(min_index, self.matrix.shape)
        print("Минимальный элемент: ", self.matrix[min_row, min_col])
        self.matrix = np.insert(self.matrix, min_row+1, self.matrix[0], axis = 0)
        print("\nМатрица после вставки:\n", self.matrix)

    def find_median_buildin(self):
        """
        Calculates the median of the first row of the matrix using NumPy's built-in function.

        Parameters:
        matrix (np.ndarray): A 2D NumPy array.

        Returns:
        float: The median of the first row.
        """
        print("Медиана 1-й строки матрицы А (встроенная ф.): ", np.median(self.matrix[0]))

    def find_median_prog(self):
        """
        Calculates the median of the first row of the matrix using a manual method.

        Parameters:
        matrix (np.ndarray): A 2D NumPy array.

        Returns:
        float: The median of the first row.
        """
        sorted_row = np.sort(self.matrix[0])
        mid = len(sorted_row) // 2

        if mid % 2 == 0:
            median = float(sorted_row[mid - 1] + sorted_row[mid]) / 2.0
        else: median = sorted_row[mid]

        print("Медиана 1-й строки (программирование формулы): ", median)
    