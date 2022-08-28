import json
class Virus:

    def __init__(self: str, name: str, long_name: str, r0: float, mortality_rate: float):
        self.name = name
        self.long_name = long_name
        self.r0 = r0
        self.mortality_rate = mortality_rate

    def get_name(self):
        return self.name

    def get_long_name(self):
        return self.long_name

    def get_r0(self):
        return self.r0

    def get_mortality_rate(self):
        return self.mortality_rate

    def __repr__(self):
        return '\n Name: {} \n Long Name: {} \n r0: {} \
                \n Mortality rate: {} '.format(self.name, self.long_name,
                                                self.r0, self.mortality_rate)

def load_viruses(file_path: str, usa_cities: list[Virus]):
    with open(file_path, 'r') as f:
        loaded_virus_list = json.load(f)
        for virus in loaded_virus_list:
            usa_cities.append(Virus( name=virus['name'],long_name=virus['long_name'],
                                    r0=virus['r0'],mortality_rate=virus['mortality_rate']))