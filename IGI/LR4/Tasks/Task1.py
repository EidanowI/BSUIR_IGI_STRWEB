def extract_words_from_file(self, filename) -> list:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split(',')
            words = [word.strip() for word in words]
        return words

class Country():
    def __init__(self, name, filename_cities):
        self.name = name
        self.cities = extract_words_from_file(filename_cities)

    

class Cities_Dict():
    def __init__(self):
        self.country_cities = {}
        
    def add_country(self, country):
        self.country_cities[country.name] = country.cities

    def add_city(self, city_name, country_name):
       for country, cities in self.country_cities.items():
            if country_name == country:
                cities.append(city_name)

    def find_country_by_city(self, city_name):
        for country, cities in self.country_cities.items():
            if city_name in cities:
                return country
        
    
    def sort_countries_by_name(self):
        self.country_cities = dict(sorted(self.country_cities.items(), key=lambda x: x[0]))
    
    def print(self):
        for country, city in self.country_cities.items():
            print(f"{country}: {city}")

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

        belarus = Country("Беларусь", "Res/belarus_ct.txt")
        
        self._country_repo.add_country(belarus)

        #self._service = ExportProductService(self._repo)
        #self._export_methods: dict[str, ExportProductFileHandler] = {
        #    'pickle': PickleExportProductFileHandler(),
        #    'csv': CSVExportProductFileHandler()
        #}
        self._filepath = filepath

    @repeating_program
    def run(self):
        """
        This method repeatedly executes a program's operations. It facilitates
        exporting data from a repository in a user-specified format, such as pickle
        or csv, and then processes the repository data by sorting and searching product
        information.

        :raise ValueError: If provided input for the export method is not valid.
        """

        try:
            export_method = input_with_validating(lambda msg: msg.lower().strip() in self._export_methods,
                                                  'Enter export method (pickle, csv): ').lower().strip()
            self._export_methods[export_method].load(self._repo, f'{self._filepath}.{export_method}')
            self._service.sort_by_country()

            print(*self._find_product_info(), sep='\n')
        except Exception as e:
            print(e)

    def _find_product_info(self):
        """
        Find product information based on user input and display the results.

        :return: The product information retrieved.
        """

        product_name = input('Enter product name: ').lower().strip()
        try:
            return self._service.find_product_info(product_name).items()
        except KeyError:
            raise KeyError('No such product exists')