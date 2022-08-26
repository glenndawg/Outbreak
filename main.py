from pprint import pprint
from Models.city import load_cities, City
from Models.event_cards import load_events, EventCard
from singletons import virus
import random


# Your code challenge is to load in all of the data for event cards and cities, 
# and use a loop inside of main.py to simulate 25 weeks with a COVID outbreak. 
# Using the classes you made previously, at the turn of each week, draw an event card 
# and apply the resulting r0 and unemployment rate changes to the applicable cities, 
# and finally apply the death rate of the virus to all infected populations. 
# You will have 1 virus object instantiated in the main method that you will use 
# throughout the simulation.

CITIES_JSON_FIXTURES_FILE_PATH = './fixtures/cities.json'
EVENT_CARDS_JSON_FIXTURES_FILE_PATH = './fixtures/event_cards.json'

week_count = 5
USA_CITIES = []
CARD_DECK = []


# r0 and unemp_rate are public instead of private
# country class? list?
# if is federal, then apply federally, then use defined function
# def apply_federally(event.card, lity_list): Change all city.r0 and city.unemp_rate

def apply_federally(event_card, city_list_for_country):
        for city in city_list_for_country:
            city.r0 += event_card.r0_difference
            city.start_unemployment_rate
            # city.unemployment_rate += event_card.unemployment_rate_difference
        return city_list_for_country

def main():

    load_cities(CITIES_JSON_FIXTURES_FILE_PATH,USA_CITIES)
    load_events(EVENT_CARDS_JSON_FIXTURES_FILE_PATH,CARD_DECK)

    for week in range(week_count):
        random_event = random.choice(CARD_DECK)
        print('Random event is {}'.format(random_event.name))
        if random_event.area_affected == 'federal':
            pprint(apply_federally(random_event, USA_CITIES))
        elif random_event.area_affected == 'local':
            random_city = random.choice(USA_CITIES)
            pprint(random_event.apply_to_affected_citie(random_city))
            # if the event is local, choose a city at random
        
if __name__ == '__main__':
    main()