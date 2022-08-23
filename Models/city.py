import random
class City:

    def __init__(self, name: str, population: str, infected_population = 0, r0 = 2):
        self.name = name
        self.population = population
        self.infected_population = infected_population
        self.r0 = r0
        
    def start_emp(self, unemp_rate = 0):
        self.unemp_rate = random.randint(7,12)

    def openhires(self, open_hires = 0):
        self.open_hires = int(round((self.unemp_rate / 100) * self.population))