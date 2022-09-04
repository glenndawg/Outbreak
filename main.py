from pprint import pprint
from wsgiref.handlers import format_date_time
from Models.city import City, load_cities_from_json, load_cities_from_csv
from Models.event_cards import load_events, EventCard
from singletons.virus import load_viruses
from singletons import virus
import random
import pandas as pd
from pandas._libs.tslibs.timestamps import Timestamp
import csv
import json
from datetime import date, datetime

CITIES_JSON_FIXTURES_FILE_PATH = "./fixtures/cities.json"
CITIES_CSV_FIXTURES_FILE_PATH = "./fixtures/cities.csv"

CITIES_JSON_DICT_FIXTURES_FILE_PATH = "./fixtures/cities_dict.json"
EVENT_CARDS_JSON_FIXTURES_FILE_PATH = "./fixtures/event_cards.json"

VIRUS_JSON_FIXTURES_FILE_PATH = "./fixtures/virus.json"

WEEK_COUNT = 52
USA_CITIES = []
CARD_DECK = []
VIRUSES = []
COUNT = 0


START_DATE = date.today()

TIME_STAMP_INDEX = pd.date_range(START_DATE, periods=WEEK_COUNT, freq="W")

# these are not necessary. Just here for learning how to create csv, and panda datafram
USA_CITIES_CHANGE = []
USA_DICT = []

def print_error_and_leave_program(error_message: str) -> None:
    print(error_message)
    exit(2)

def apply_federally(event_card, city_list_for_country):
    for city in city_list_for_country:
        city.r0 += event_card.r0_difference
        city.unemployment_rate += event_card.unemployment_rate_difference
        city.start_infection_rate()
        city.calculate_open_hires()
        if event_card.event_type == "mutation":
            for virus in VIRUSES:
                if virus.name == event_card.name:
                    event_card.apply_mortality_rate(city)

def save_cities_to_csv(usa_cities):
    with open("cities.csv", "w") as data_frame_cities:
        writer = csv.writer(data_frame_cities)
        # Can I add an index value to count weeks like my pd ????
        writer.writerow(
            ["name", "population", "infect_pop", "r0", "unemp_rate", "open_hires", "deaths"]
        )
        writer.writerows(usa_cities)

def create_data_frame(usa_cities):
    pd.set_option(
        "display.max_rows", None, "display.max_columns", None, "display.width", 200
    )
    headers = [
        "name",
        "population",
        "infect_pop",
        "r0",
        "unemp_rate",
        "open_hires",
        "deaths",
    ]
    df = pd.DataFrame(usa_cities)
    df.columns = headers
    df.to_csv("cities_pd.csv", header=headers, sep=",")

def load_cities_to_dictionary(file_path: str):
    with open(file_path, "r") as f:
        usa_dict = json.load(f)
    return usa_dict

def create_time_series(usa_dict, city_from_usa_cities, count):
    for city in usa_dict:
        if city['name'] == city_from_usa_cities.name:
            city['infected_population'].append(city_from_usa_cities.infected_population)
            city['r0'].append(city_from_usa_cities.r0)
            city['unemployment_rate'].append(city_from_usa_cities.unemployment_rate)
            city['open_hires'].append(city_from_usa_cities.open_hires)
            city['deaths'].append(city_from_usa_cities.deaths)
            city['week'].append(TIME_STAMP_INDEX[count])

def humanize_time_series(usa_dict):
    format_date = ('%y-%m-%s')
    for city in usa_dict:
        for key, value in city.items():
            if key == 'r0':
                for num in range(len(value)):
                    value[num] = round(value[num], 2)
            if key == 'unemployment_rate':
                for num in range(len(value)):
                    value[num] = round(value[num], 2)
            if key == 'week':
                for num in range(len(value)):
                    ts = Timestamp(value[num])
                    value[num] = ts.to_pydatetime()
                    value[num] = value[num].date()
                    
    return usa_dict

def get_user_input():
    # file_load_format = input('Load cities from JSON, or CSV ? :')
    file_load_format = "JSON"

    try:
        if file_load_format.lower() == "json":
            load_cities_from_json(CITIES_JSON_FIXTURES_FILE_PATH, USA_CITIES)
        elif file_load_format.lower() == "csv":
            load_cities_from_csv(CITIES_CSV_FIXTURES_FILE_PATH, USA_CITIES)
        else:
            raise ValueError("Must choose one of (JSON or csv) ")
    except ValueError as ve:
        print_error_and_leave_program(ve)

def main(COUNT):

  
    get_user_input()

    USA_DICT = load_cities_to_dictionary(CITIES_JSON_DICT_FIXTURES_FILE_PATH)
    load_events(EVENT_CARDS_JSON_FIXTURES_FILE_PATH, CARD_DECK)
    load_viruses(VIRUS_JSON_FIXTURES_FILE_PATH, VIRUSES)

    for city in USA_CITIES:  # set unemployment rates for each city
        city.start_unemployment_rate()

    for week in range(WEEK_COUNT): 
        
        # each week, pick a random event  
        random_event = random.choice(CARD_DECK) # use this line when doen with the below test
        # random_event = CARD_DECK[1] # this is temporary, to drive a specific event for testing
        if random_event.area_affected == "federal":
            apply_federally(random_event, USA_CITIES)
            for city in USA_CITIES:
                USA_CITIES_CHANGE.append(city)
                create_time_series(USA_DICT, city, COUNT)

        elif random_event.area_affected == "local":
            for city in USA_CITIES:
                if city.name in random_event.affected_cities:
                    random_event.apply_to_affected_citie(city)
                    USA_CITIES_CHANGE.append(city)
                    create_time_series(USA_DICT,city, COUNT)
        COUNT += 1 

    for city in USA_CITIES_CHANGE:
        city.round_values()

    humanize_time_series(USA_DICT)

    create_data_frame(USA_CITIES_CHANGE)
    save_cities_to_csv(USA_CITIES_CHANGE)

    for city in USA_DICT:
        pprint(city)

    

       

if __name__ == "__main__":
    main(COUNT)
