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