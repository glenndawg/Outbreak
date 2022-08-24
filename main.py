from Models import city , event_cards
from singletons import virus

import random
from decimal import ROUND_05UP
from unicodedata import name

# Your code challenge is to load in all of the data for event cards and cities, 
# and use a loop inside of main.py to simulate 25 weeks with a COVID outbreak. 
# Using the classes you made previously, at the turn of each week, draw an event card 
# and apply the resulting r0 and unemployment rate changes to the applicable cities, 
# and finally apply the death rate of the virus to all infected populations. 
# You will have 1 virus object instantiated in the main method that you will use 
# throughout the simulation.

week_count = 25
city_list = []

# country class? list?
# if is federal, then apply federally, then use defined function
# def apply_federally(event.card, lity_list): Change all city.r0 and city.unemp_rate

def main():
    for week in range(len(week_count)):



if __name__ == '__main__':
    main()