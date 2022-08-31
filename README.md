# Outbreak
Solve stack project

Create Classes

Class City:
# Make a city class with the following private instance variables:
# name
# population
# infected_population
# r0 - Spread factor in the City location
# unemployment rate
# open hires

# Make the following instance methods:
# Init method - takes in name and population,
# saves the name and population as instance variables
# then randomizes the starting unemployment rate between 7 and 12%,
# saves that unemployment rate to the instance variable, and
# applies that unemployment rate to the population, and sets it as the open hires private instance variable

Event Class:
# write a class to represent an eventcard in the game with the following private instance variables:
# name - "riots with mask burning"
# event type (mandate, mutation, or public unrest)
# area_affected - one of either "local" or "federal"
# r0 difference - Difference to the spread factor in the City location
# unemployment rate difference - Difference to the unemployment rate in the city location

# Methods
# Init method: takes in name, event type, area_affected, r0 difference, and
# unemployment rate difference and saves them all to private attributes

# apply_to_affected_cities(city): takes in a city and changes its r0 by the
#    r0 difference private attribute, changes the city's unemployment rate by the 
# unemployment rate difference

Virus Class:
# write a Virus class with the following:

Instance variables:
# Name - name of the virus, I.E. COVID-19
# Long name - name of the virus, I.E. Sars-cov-2 -->
# R0 - the average number of people who will contract a contagious disease from one person with that disease
# See this site for more info: https://www.healthline.com/health/r-nought-reproduction-number
# mortality rate- https://www.worldometers.info/coronavirus/coronavirus-death-rate/

# Init method:
# takes in Name, Long name, R0, and mortality rate and sets them as private attributes

# Getter Methods:
# get_name: gets the private attribute name
# get_long_name: gets the private attribute long name
# get_r0(): gets the private attribute r0
# get_mortality_rate(): gets the private attribute mortality rate

First Assignement:

Git Submission: Outbreak
For this assignment, you will do the following steps:
Create a username and git repository in Github. Give your teachers write access: icepuente and tomboolean
Take the classes that you built in Week 5 and do an initial commit with them in the folder structure you will find below. Push these to the new repo you created.
├── LICENSE

├── README.md

├── fixtures

 │   ├── __init__.py

 │   ├── cities.csv

 │   ├── cities.json

 │   ├── event_cards.csv

 │   └── event_cards.json

├── main.py

├── singletons

 │   ├── __init__.py

 │  └── virus.py

├── models

 │   ├── __init__.py

 │   ├── city.py

 │   └── event_cards.py

Create a new branch off of main to make your changes for this assignment, and submit a pull request to your repository
Your instructor will provide dummy data in ./fixtures/event_cards.json and ./fixtures/event_cards.csv, for the event cards. Populate a global variable in main.py called CARD_DECK as a list of the event cards.

Your instructor will provide dummy data in ./fixtures/cities.json and ./fixtures/cities.csv, for the cities. Populate a global variable in main.py called USA_CITIES as a list of the cities.

In main.py, you will accept user input, and define a function that applies the event card information to the whole country. This function signature is the following:

apply_federally(event_card, city_list_for_country): changes the following for all cities:

the city's r0 by the r0 difference public instance attribute in EventCard
the city's r0 unemployment rate by the unemployment rate difference public instance attribute in EventCard
Using this and the classes you defined previously, your code challenge is to load in all of the data for event cards and cities, and use a loop inside of main.py to simulate 25 weeks with a COVID outbreak.

Using the classes you made previously, at the turn of each week, draw an event card and apply the resulting r0 and unemployment rate changes to the applicable cities, and finally apply the death rate of the virus to all infected populations. You will have 1 virus object instantiated in the main method that you will use throughout the simulation.



