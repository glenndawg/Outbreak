from math import trunc
import random
import json
import csv
class City:

    def __init__(self, name: str, population: int, infected_population = 0, r0 = 0.0, unemployment_rate = 0.0, open_hires = 0, deaths = 0):
        self.name = name
        self.population = population
        self.infected_population = infected_population
        self.r0 = r0
        self.unemployment_rate = round(unemployment_rate)
        self.open_hires = open_hires
        self.deaths = deaths
        
    def start_unemployment_rate(self):
        self.unemployment_rate = int(random.randint(7,12))
#  unemployment_rate: float, open_hires: float
    def calculate_open_hires(self):
        self.open_hires = round(((self.unemployment_rate / 100) * self.population))

    def start_infection_rate(self):
        self.infected_population = round(random.randint(10,80)/100 * self.population)

    def __repr__(self):
        return '\n Name: {} \n Population: {} \n Infected Population: {} \n r0: {} \
                  \n Unemployment rate: {} \n Open hires: {} \n Deaths: {}' \
                  .format(self.name, self.population, self.infected_population,
                    round(self.r0,2), round(self.unemployment_rate,2), self.open_hires, self.deaths)
                                                                
    def __iter__(self):
        return iter([self.name, self.population, self.infected_population, self.r0,
                        self.unemployment_rate, self.open_hires, self.deaths])

    def round_values(self):
            self.name = self.name
            self.population = int(self.population)
            self.infected_population = int(self.infected_population)
            self.r0 = round(self.r0,2)
            self.unemployment_rate = round(self.unemployment_rate,2)
            self.open_hires = int(self.open_hires)
            self.deaths = int(self.deaths)

def load_cities_from_json(file_path: str, usa_cities: list[City]):
    with open(file_path, 'r') as f:
        loaded_cities_list = json.load(f)
        for city in loaded_cities_list:
            usa_cities.append(City( name=city['name'],
                                    population=city['population'],
                                    r0=city['r0']))

def load_cities_from_csv(file_path: str, usa_cities: list[City]):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        loaded_cities_list = list(reader)
        for city in loaded_cities_list:
            print(city)
            usa_cities.append(City( name=city[0],
                                    population=int(city[1]),
                                    r0=float(city[2])))

        