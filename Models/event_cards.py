class EventCard:

    def __init__(self, name: str, event_type: str, area_affected: str, r0_diff: float, unemp_rate_dif: float):
        self.name = name
        self.event_type = event_type
        self.area_affected = area_affected
        self.r0_diff = r0_diff
        self.unemp_rate_dif = unemp_rate_dif

    def apply_to_affected_cities(self, City):
        City.r0 = City.r0 - self.r0_diff
        City.unemp_rate = City.unemp_rate - self.unemp_rate_dif
        return City.r0 , City.unemp_rate

    def apply_federally(cls, self):
        pass
        # self.unemp_rate = self.unemp_rate - self.unemp_rate_dif