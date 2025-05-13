import numpy as np

class Statistics:
    """Class for statistical computations on matrices."""
    def __init__(self):
        pass

    @staticmethod
    def mean(matrix):
        """Calculate the mean of the matrix."""
        return np.mean(matrix)

    @staticmethod
    def median(matrix):
        """Calculate the median of the matrix."""
        return np.median(matrix)

    @staticmethod
    def variance(matrix):
        """Calculate the variance of the matrix."""
        return np.var(matrix)

    @staticmethod
    def std_dev(matrix):
        """Calculate the standard deviation of the matrix."""
        return np.std(matrix)

    @staticmethod
    def correlation(matrix, col1, col2):
        """Calculate correlation between two columns."""
        return round(np.corrcoef(matrix[:, col1], matrix[:, col2])[0, 1], 2)