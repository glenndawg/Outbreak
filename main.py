from pprint import pprint
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
from plot import line_plot

CITIES_JSON_FIXTURES_FILE_PATH = "./fixtures/cities.json"
CITIES_CSV_FIXTURES_FILE_PATH = "./fixtures/cities.csv"
CITIES_JSON_DICT_FIXTURES_FILE_PATH = "./fixtures/cities_dict.json"

EVENT_CARDS_JSON_FIXTURES_FILE_PATH = "./fixtures/event_cards.json"
VIRUS_JSON_FIXTURES_FILE_PATH = "./fixtures/virus.json"

WEEK_COUNT = 27

USA_CITIES = []
CARD_DECK = []
VIRUSES = []

START_DATE = date.today()
TIME_STAMP_INDEX = pd.date_range(START_DATE, periods=WEEK_COUNT, freq="W")
USA_CITIES_DICT = []

# these are not necessary. Just here for learning how to create csv, and panda datafram
USA_CITIES_CHANGE = []

def get_user_input_for_import_type():

    
    # file_load_format = "JSON"
    while True: # 
        try:
            file_load_format = input('Load cities from JSON, or CSV ? :')
            if file_load_format.lower() == "json":
                load_cities_from_json(CITIES_JSON_FIXTURES_FILE_PATH, USA_CITIES)
            elif file_load_format.lower() == "csv":
                load_cities_from_csv(CITIES_CSV_FIXTURES_FILE_PATH, USA_CITIES)
            else:
                raise ValueError("Must choose one of (JSON or CSV) ")
            break
        except ValueError:
            print('Please eneter JSON or CSV')

def load_cities_to_dictionary(file_path: str) -> dict:
    with open(file_path, "r") as f:
        usa_cities_dict = json.load(f)
    return usa_cities_dict

def initialize_time_series_weeks(usa_cities_dict: list[dict[list]]):
    for city in usa_cities_dict:
        city['week'].append(START_DATE)

def build_time_series_weeks(usa_cities_dict: list[dict[list]], city_from_usa_cities: City, week: int):
    for city in usa_cities_dict:
        if city['name'] == city_from_usa_cities.name:
            city['infected_population'].append(city_from_usa_cities.infected_population)
            city['r0'].append(city_from_usa_cities.r0)
            city['unemployment_rate'].append(city_from_usa_cities.unemployment_rate)
            city['open_hires'].append(city_from_usa_cities.open_hires)
            city['deaths'].append(city_from_usa_cities.deaths)
            city['week'].append(TIME_STAMP_INDEX[week])

def apply_federally(event_card: EventCard, city_list_for_country: City):
    for city in city_list_for_country:
        city.r0 += event_card.r0_difference
        city.unemployment_rate += event_card.unemployment_rate_difference
        city.start_infection_rate()
        city.calculate_open_hires()
        if event_card.event_type == "mutation":
            for virus in VIRUSES:
                if virus.name == event_card.name:
                    event_card.apply_mortality_rate_and_r0(city, virus)

def humanize_time_series(usa_cities_dict: list[dict[list]]):
    format_date = ('%y-%m-%s')
    for city in usa_cities_dict:
        for key, value in city.items():
            if key == 'r0':
                for num in range(len(value)):
                    value[num] = round(value[num], 2)
            if key == 'unemployment_rate':
                for num in range(len(value)):
                    value[num] = round(value[num], 2)
            if key == 'week':
                # value[0] = START_DATE
                for num in range(0,len(value)):
                    ts = Timestamp(value[num])
                    value[num] = ts.to_pydatetime()
                    value[num] = value[num].date()                  
    return usa_cities_dict

def save_cities_to_csv(usa_cities_dict: list[dict[list]]): # this is not working yet, mostly notes here
    with open("cities.csv", "w", newline='') as data_frame_cities:
        headers = usa_cities_dict[0].keys()
        writer = csv.writer(data_frame_cities)
        # writer.writerows()
        writer.writerow(
             ["name", "population", "infect_pop", "r0", "unemp_rate", "open_hires", "deaths","week"]
         )
        for city in usa_cities_dict: # city is a dict in the list usa_cities_dict
            # for key, value in city.items(): # key, value in the city dict
            #         writer.writerow('key')
            for key, vals in sorted(city.items(), key=lambda k: k[0]):
                writer.writerow([key] + vals[1])
                    # print(key)
                    # print(type(key))
                    # print(value)
                    # print(type(value))

                # writer.writerow([value[0]])
                # if key == 'r0':
                #     for num in range(len(value)):
                #         writer.writerow()
                # writer.writerow(str.join(',',+ [value[i] for i in value]))
                 # +[str(i) for i in value])+'\n')

def create_data_frame(usa_cities: City): # does not represent the tie series - only final values
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

def get_data_to_plot(usa_cities_dict: list[dict[list]]): # ask for user input, then send data to plot

    city = None
    category = None
    
    # this could be created like the city_name_dict in case more attributes are added in the future
    # fix the attributes input/out put here. Too many magic strings, and still clunky
    attributes_names ={1:'Infected Population',2:'r0',3:'Unemployment Rate',4:'Open Hires',5:'deaths'}

    city_names = []
    number_range = []
    city_name_dict ={}

    weeks = [] # x - axis
    attributes = [] # y - axis
    
    for item in usa_cities_dict: # create a list of city names for display
        city_names.append(item['name'])
    for number in range(1,len(usa_cities_dict)+1): # creat list of numbers to zip with names
        number_range.append(number)
    city_name_dict = dict(zip(number_range, city_names))


    for key, value in city_name_dict.items(): # display list of cities to select from
        print(key, ': ', value)

    while True: # get input for city selection
        try:
            city_num = int(input("Please enter the number of the city you would like to graph : "))
            if city_num > len(usa_cities_dict) or city_num < 1:
                raise ValueError
            break
        except ValueError:
            print(f'Please enter a whole number less than or equal to {len(usa_cities_dict)}')

    for key, value in attributes_names.items(): # create a list of city attributes for display
        print(key,': ', value)

    while True: # get input for attribute selection
        try:
            category_num = int(input('Please enter the number of the attribute you would like to graph : '))
            if category_num == 1:
                category = 'infected_population'
            elif category_num == 2:
                category = 'r0'
            elif category_num == 3:
                category = 'unemployment_rate'
            elif category_num == 4:
                category = 'open_hires'
            elif category_num == 5:
                category = 'deaths'
            if category_num > len(attributes_names) or category_num < 1:
                raise ValueError
            break
        except ValueError:
            print(f'Please enter a whole number less than or equal to {len(attributes_names)}')

    for key, value in city_name_dict.items():
        if key == city_num:
            city = value

    for item in usa_cities_dict:
        if item['name'] == city:
            for key, value in item.items():
                if key == category:
                    attributes.append(value)
                elif key == 'week':
                    weeks.append(value)
        
    line_plot(weeks, attributes, city, category)


def main():

    get_user_input_for_import_type()

    USA_CITIES_DICT = load_cities_to_dictionary(CITIES_JSON_DICT_FIXTURES_FILE_PATH)
    load_events(EVENT_CARDS_JSON_FIXTURES_FILE_PATH, CARD_DECK)
    load_viruses(VIRUS_JSON_FIXTURES_FILE_PATH, VIRUSES)

    for city in USA_CITIES:  # set unemployment rates for each city
        city.start_unemployment_rate()

    initialize_time_series_weeks(USA_CITIES_DICT) # assign the first date to week

    for week in range(WEEK_COUNT): 
    
        # each week, pick a random event  
        random_event = random.choice(CARD_DECK) # use this line when doen with the below test
        # random_event = CARD_DECK[1] # this is temporary, to drive a specific event for testing
        if random_event.area_affected == "federal":
            apply_federally(random_event, USA_CITIES)
            for city in USA_CITIES:
                USA_CITIES_CHANGE.append(city) # this will be delete
                build_time_series_weeks(USA_CITIES_DICT, city, week)

        elif random_event.area_affected == "local":
            for city in USA_CITIES:
                if city.name in random_event.affected_cities:
                    random_event.apply_to_affected_citie(city)
                    USA_CITIES_CHANGE.append(city) # this will be delete
                    build_time_series_weeks(USA_CITIES_DICT,city, week)

    for city in USA_CITIES_CHANGE: 
        city.round_values()
    
    humanize_time_series(USA_CITIES_DICT)
    create_data_frame(USA_CITIES_CHANGE)
    # save_cities_to_csv(USA_CITIES_DICT) # this is still under construction

    # for city in USA_CITIES_DICT: # this is here for output testing when needed
    #     pprint(city)

    get_data_to_plot(USA_CITIES_DICT)

if __name__ == "__main__":
    main()
