from pprint import pprint
from Models.city import City, load_cities_from_json, load_cities_from_csv
from Models.event_cards import load_events, EventCard
from singletons.virus import load_viruses
from singletons import virus
import random
import pandas as pd
import csv

CITIES_JSON_FIXTURES_FILE_PATH = './fixtures/cities.json'
CITIES_CSV_FIXTURES_FILE_PATH = './fixtures/cities.csv'
EVENT_CARDS_JSON_FIXTURES_FILE_PATH = './fixtures/event_cards.json'
VIRUS_JSON_FIXTURES_FILE_PATH = './fixtures/virus.json'

week_count = 25
USA_CITIES = []
CARD_DECK = []
VIRUSES = []
USA_CITIES_CHANGE = []

def print_error_and_leave_program(error_message: str) -> None:
    print(error_message)
    exit(2)

def apply_federally(event_card, city_list_for_country):
        for city in city_list_for_country:
            city.r0 += event_card.r0_difference
            city.unemployment_rate += event_card.unemployment_rate_difference
            city.start_infection_rate()
            city.calculate_open_hires()
            USA_CITIES_CHANGE.append(city)
            if event_card.event_type == 'mutation':
                for virus in VIRUSES:
                    if virus.name == event_card.name:
                        event_card.apply_mortality_rate(city)
                        USA_CITIES_CHANGE.append(city)

def save_cities(usa_cities):
    with open('cities.csv', 'w') as data_frame_cities:
        writer = csv.writer(data_frame_cities)
        # Can I add an index value to count weeks like my pd ????
        writer.writerow(['name','population','infect_pop','r0','unemp_rate','open_hires'])
        writer.writerows(usa_cities)

def create_df(usa_cities):
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", 200)
    headers = ['name', 'population', 'infect_pop','r0','unemp_rate', 'open_hires', 'deaths']
    df = pd.DataFrame(usa_cities)
    df.columns = headers
    df.to_csv('cities_pd.csv', header=headers, sep=',')

def main():
    # file_load_format = input('Load cities from JSON, or CSV ? :')
    file_load_format = 'JSON'

    try:
        if file_load_format.lower() == 'json':
            load_cities_from_json(CITIES_JSON_FIXTURES_FILE_PATH, USA_CITIES)
        elif file_load_format.lower() == 'csv':   
            load_cities_from_csv(CITIES_CSV_FIXTURES_FILE_PATH, USA_CITIES)
        else:
            raise ValueError("Must choose one of (JSON or csv) ")
    except ValueError as ve:
        print_error_and_leave_program(ve)

    load_events(EVENT_CARDS_JSON_FIXTURES_FILE_PATH,CARD_DECK)
    load_viruses(VIRUS_JSON_FIXTURES_FILE_PATH,VIRUSES)

    for city in USA_CITIES:             # set unemployment rates for each city
        city.start_unemployment_rate()
   
    for week in range(week_count):       # each week, pick a random event
        random_event = random.choice(CARD_DECK)
        
        if random_event.area_affected == 'federal':
            apply_federally(random_event, USA_CITIES)
                 
        elif random_event.area_affected == 'local':
            for city in USA_CITIES:
                if city.name in random_event.affected_cities:
                    random_event.apply_to_affected_citie(city)
                    USA_CITIES_CHANGE.append(city)
    
    for city in USA_CITIES_CHANGE:
        city.round_values()

    create_df(USA_CITIES_CHANGE) 
    save_cities(USA_CITIES_CHANGE)   

    for citi in USA_CITIES:
        pprint(citi)
             
if __name__ == '__main__':
    main()