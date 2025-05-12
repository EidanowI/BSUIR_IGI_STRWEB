"""
Lab №4
Completed by Fyodor Kovalchuck, group 353504.
variant 12
The program presents work with classes, serializers, regular expressions, standard libraries.
v1.0
Development date:
10.05.2025
"""

#from ..Utils.input import input_positive_int
from .ITask import ITask
import csv, pickle

class Country():
    """
    Represents a country with its name and a list of cities.

    Attributes:
    - name (str): The name of the country.
    - cities (list): A list of cities in the country.

    Methods:
    - __init__(name, cities): Initializes a new instance of the Country class.
    """
    def __init__(self, name, cities):
        """
        Initializes a new instance of the Country class.

        Parameters:
        - name (str): The name of the country.
        - cities (list): A list of cities associated with the country.
        """
        self.name = name
        self.cities = cities

    

class Cities_Dict():
    """
    A class to manage a dictionary of countries and their cities.

    Attributes:
    - country_cities (dict): A dictionary where keys are country names 
                             and values are lists of cities in those countries.

    Methods:
    - __init__(): Initializes a new instance of the Cities_Dict class.
    - add_country(country): Adds a country and its associated cities to the dictionary.
    - add_city(city_name, country_name): Adds a city to the specified country.
    """
    def __init__(self):
        """
        Initializes a new instance of the Cities_Dict class.

        The constructor initializes an empty dictionary to store country names 
        and their corresponding lists of cities.
        """
        self.country_cities = {}
        
    def add_country(self, country):
        """
        Adds a country and its associated cities to the dictionary.

        Parameters:
        - country (Country): An instance of the Country class containing 
                             the country name and its cities.
        """
        self.country_cities[country.name] = country.cities

    def add_city(self, city_name, country_name):
       """
        Adds a city to the specified country.

        Parameters:
        - city_name (str): The name of the city to be added.
        - country_name (str): The name of the country to which the city will be added.

        If the country exists, the city is appended to its list of cities.
        """
       for country, cities in self.country_cities.items():
            if country_name == country:
                cities.append(city_name)

    def find_country_by_city(self, city_name):
        """
        Finds the country associated with a given city name.

        This function searches through a dictionary of countries and their corresponding
        cities to locate the country that contains the specified city.

        Parameters:
        ----------
        city_name : str
            The name of the city to search for.

        Returns:
        -------
        str
            The name of the country associated with the city if found.

        Raises:
        ------
        ValueError
            If the city name is not found in any country.
        """
        for country, cities in self.country_cities.items():
            if city_name in cities:
                return country
        
    
    def sort_countries_by_name(self):
        """
        Sorts the countries and their associated cities alphabetically.

        Updates the country_cities dictionary to have the countries sorted by name,
        and each list of cities sorted alphabetically.
        """
        self.country_cities = {key: sorted(value) for key, value in sorted(self.country_cities.items())}
        #self.country_cities = dict(sorted(self.country_cities.items(), key=lambda x: x[0]))
    
    def print(self):
        """
        Prints the countries and their associated cities.

        Each country is printed on a new line, followed by its list of cities.
        """
        for country, city in self.country_cities.items():
            print(f"{country}: {city}")

    def save_to_scv(self, path):
        """
        Saves the countries and their cities to a CSV file.

        Parameters:
        - path (str): The file path where the CSV file will be saved.
        """
        with open(path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for country, cities in self.country_cities.items():
                writer.writerow([country, ", ".join(cities)])

    def save_to_pickle(self, path):
        """
        Saves the countries and their cities to a pickle file.

        Parameters:
        - path (str): The file path where the pickle file will be saved.
        """
        with open(path, "wb") as file:
            pickle.dump(self.country_cities, file)

    def read_from_csv(self, path):
        """
        Reads countries and cities from a CSV file and adds them to the dictionary.

        Parameters:
        - path (str): The file path from which the CSV file will be read.
        """
        data_lst = list()

        with open(path, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                country_name = row[0]
                cities_name = row[1].split(", ")
                data = Country('', [])
                data.name = country_name
                data.cities = cities_name 
                data_lst.append(data)

        for data in data_lst:
            if data.name not in self.country_cities.keys():
                self.add_country(data)
            else: continue



class Task1(ITask):
    """
    The source data in the form of a dictionary are placed in files (pickle and csv).
    Data reading, searching, and sorting are organized.
    The summary of exported goods indicates: the name of the product, the country exporting the product,
    the volume of the supplied batch in pieces. A list of countries to which the product is exported and
    the total volume of its export are printed. Information about the product entered from the keyboard displayed.
    """

    def __init__(self, filepath: str):
        self._country_repo = Cities_Dict()

        self._country_repo.read_from_csv(filepath + "res.csv")

        self._filepath = filepath

    def run(self):
        """
        This method repeatedly executes a program's operations. It facilitates
        exporting data from a repository in a user-specified format, such as pickle
        or csv, and then processes the repository data by sorting and searching product
        information.

        :raise ValueError: If provided input for the export method is not valid.
        """

        while True:
            print("\nМеню выбора действия:")

            print("1. Найти, в какой стране расположен город")
            print("2. Отсортировать страны по алфавиту")
            print("3. Вывести все страны и их города")
            print("4. Добавить город")
            print("5. Сохранить в CSV")
            print("6. Сохранить в pickle")
            print("7. Считать c CSV")
            print("0. Выход")

            choice = input("Выберите задание (0-5): ").strip()
            
            if choice == '0':
                break
            elif choice == '1':
                city = input("Введите город: ")
                country = self._country_repo.find_country_by_city(city)
                print(f"Страна: {country}")              
            elif choice == '2':
                self._country_repo.sort_countries_by_name()
                self._country_repo.print()           
            elif choice == '3':
                 self._country_repo.print()      
            elif choice == '4':
                city = input("Введите город: ")
                country = self._country_repo.find_country_by_city(city)
                if country == None: 
                    country = input("Введите страну: ")
                    self._country_repo.add_city(city, country)
                else: print("Город уже добавлен")
            elif choice == '5':
                self._country_repo.save_to_scv(self._filepath + "res.csv")
            elif choice == '6':
                self._country_repo.save_to_pickle(self._filepath + "res.pickle")
            elif choice == '7':
                self._country_repo.read_from_csv(self._filepath + "res.csv")
            else:
                print("Неверный выбор. Пожалуйста, выберите снова.")