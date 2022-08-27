from operator import index
from pprint import pprint
from Models.city import load_cities, City
from Models.event_cards import load_events, EventCard
from singletons import virus
import random
import pandas as pd
import csv


CITIES_JSON_FIXTURES_FILE_PATH = './fixtures/cities.json'
EVENT_CARDS_JSON_FIXTURES_FILE_PATH = './fixtures/event_cards.json'

week_count = 25
USA_CITIES = []
CARD_DECK = []
USA_CITIES_CHANGE = []

def apply_federally(event_card, city_list_for_country):
        for city in city_list_for_country:
            city.r0 += event_card.r0_difference
            city.start_unemployment_rate
            city.unemployment_rate += event_card.unemployment_rate_difference
            city.start_infection_rate()
            city.calculate_open_hires()
            if event_card.event_type == 'mutation':
                event_card.apply_mortality_rate(city)
            USA_CITIES_CHANGE.append(city)
        return city_list_for_country

def save_cities(usa_cities):
    # headers = ['name', 'population', 'infected_population','r0','unemployment_rate', 'open_hires']
    with open('cities.csv', 'w') as data_frame_cities:
        writer = csv.writer(data_frame_cities)
        writer.writerows(usa_cities)
         
def main():

    load_cities(CITIES_JSON_FIXTURES_FILE_PATH,USA_CITIES)
    load_events(EVENT_CARDS_JSON_FIXTURES_FILE_PATH,CARD_DECK)

    # set unemployment rates for each city
    for city in USA_CITIES:
        city.start_unemployment_rate()
    # each week, pick a random event, and then apply it to local or federal
    for week in range(week_count):
        random_event = random.choice(CARD_DECK)
        # print('Random event is {}'.format(random_event.name))
        if random_event.area_affected == 'federal':
            apply_federally(random_event, USA_CITIES)
                    
        elif random_event.area_affected == 'local':
            for city in  USA_CITIES:
                if city.name in random_event.affected_cities:
                    random_event.apply_to_affected_citie(city)
                    USA_CITIES_CHANGE.append(city)

    save_cities(USA_CITIES_CHANGE)                  
    for city in USA_CITIES:
        print(city)

if __name__ == '__main__':
    main()