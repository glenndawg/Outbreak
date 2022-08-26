import random
import json
class City:

    def __init__(self, name: str, population: str, infected_population = 0.0, r0 = 0.0, unemployment_rate = 0.0, open_hires = 0):
        self.name = name
        self.population = population
        self.infected_population = infected_population
        self.r0 = r0
        self.unemployment_rate = unemployment_rate
        self.open_hires = open_hires
        
    def start_unemployment_rate(self):
        self.unemployment_rate = random.randint(7,12)
#  unemployment_rate: float, open_hires: float
    def calculate_open_hires(self):
        self.open_hires = round(((self.unemployment_rate / 100) * self.population),2)

    def __repr__(self):
        return '\n Name: {} \n Population: {} \n Infected Population: {} \n r0: {} \
                  \n Unemployment rate: {} \n Open hires: {} \n'.format( self.name,
                                                                self.population,
                                                                self.infected_population,
                                                                round(self.r0,2),
                                                                round(self.unemployment_rate,2),
                                                                self.open_hires)

def load_cities(file_path: str, usa_cities: list[City]):
    with open(file_path, 'r') as f:
        loaded_cities_list = json.load(f)
        for city in loaded_cities_list:
            usa_cities.append(City( name=city['name'],
                                    population=city['population'],
                                    r0=city['r0']))

        