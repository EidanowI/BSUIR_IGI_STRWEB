"""
Lab №4
Completed by Fyodor Kovalchuck, group 353504.
variant 12
The program presents work with classes, serializers, regular expressions, standard libraries.
v1.0
Development date:
10.05.2025
"""

from abc import abstractmethod, ABC

class ITask(ABC):
    """
    Abstract class for defining the interface of a task.

    This class serves as a base for all tasks that must implement 
    the run() method. Classes inheriting from ITask are required 
    to provide a concrete implementation of this method.

    Methods:
    - run(): Executes the task. The specific implementation must be provided 
             in subclasses.
    """

    @abstractmethod
    def run(self): 
        """
        Executes the task.

        This method must be implemented in subclasses.
        """
        ...