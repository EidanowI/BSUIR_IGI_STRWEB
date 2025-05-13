"""
Lab №4
Completed by Fyodor Kovalchuck, group 353504.
variant 12
The program presents work with classes, serializers, regular expressions, standard libraries.
v1.0
Development date:
10.05.2025
"""

from Tasks.ITask import ITask
from Tasks.Task1 import Task1
from Tasks.Task2 import Task2
from Tasks.Task3 import Task3
from Tasks.Task4 import Task4
from Tasks.Task5 import Task5

class Menu(object):
    def __init__(self):
        self.tasks: dict[str, ITask] = {
            '1': Task1(filepath='data/Task1/'),
            '2': Task2(filepath='data/Task2/'),
            '3': Task3(filepath='data/Task3/'),
            '4': Task4(filepath='data/Task4/'),
            '5': Task5(),
        }

    def show(self):
        while True:
            choice = input('\nComplete task - 1..5'
                           '\nShow task condition - 1d..5d'
                           '\nExit - 0\n').strip()

            match choice:
                case cmd if cmd in self.tasks:
                    self.tasks[cmd].run()
                case cmd if cmd.endswith('d') and (num := cmd[:-1]) in self.tasks:
                    print(self.tasks[num].__doc__)
                case '0':
                    break
                case _:
                    print('Invalid choice.')


if __name__ == '__main__':
    menu = Menu()
    menu.show()