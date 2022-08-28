import json

class EventCard:

    def __init__(self, name: str, event_type: str, area_affected: str, r0_difference: float, unemployment_rate_difference: float, affected_cities: str):
        self.name = name
        self.event_type = event_type
        self.area_affected = area_affected
        self.r0_difference = r0_difference
        self.unemployment_rate_difference = unemployment_rate_difference
        self.affected_cities = affected_cities

    def apply_to_affected_citie(self, City):
        City.r0 += self.r0_difference
        City.unemployment_rate += self.unemployment_rate_difference
        City.start_infection_rate()
        return City

    def apply_mortality_rate(self, City):
        City.deaths = round(0.008 * City.infected_population)
        
    def __repr__(self):
        return 'Name: {} \n Event type: {} \n Area affected: {} \n r0 difference: {} \
                \n Unemployment change: {} \n Affected Cities: {}'.format(self.name, self.event_type,
                                                self.area_affected, self.r0_difference,
                                                self.unemployment_rate_difference,
                                                self.affected_cities)

def load_events(file_path: str, card_deck: list[EventCard]):
    with open(file_path, 'r') as f:
        loaded_events_list = json.load(f)
        for event in loaded_events_list:
            card_deck.append(EventCard( name = event['name'], 
                                            event_type=event["event_type"], 
                                            area_affected=event["area_affected"], 
                                            r0_difference=event["r0_difference"],
                                            unemployment_rate_difference=event['unemployment_rate_difference'],
                                            affected_cities=event['affected_cities']))