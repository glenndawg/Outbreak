# Outbreak
Solve stack project

# Create Classes --> 

# Class City:
Make a city class with the following private instance variables:
name
population
infected_population
r0 - Spread factor in the City location
unemployment rate
open hires

Make the following instance methods:
Init method - takes in name and population,
saves the name and population as instance variables
then randomizes the starting unemployment rate between 7 and 12%,
saves that unemployment rate to the instance variable, and
applies that unemployment rate to the population, and sets it as the open hires private instance variable

# Event Class:
write a class to represent an eventcard in the game with the following private instance variables:
name - "riots with mask burning"
event type (mandate, mutation, or public unrest)
area_affected - one of either "local" or "federal"
r0 difference - Difference to the spread factor in the City location -->
unemployment rate difference - Difference to the unemployment rate in the city location

# Methods
Init method: takes in name, event type, area_affected, r0 difference, and
unemployment rate difference and saves them all to private attributes

# apply_to_affected_cities(city): takes in a city and changes its r0 by the
r0 difference private attribute, changes the city's unemployment rate by the 
unemployment rate difference

# Virus Class:
write a Virus class with the following:

# Instance variables:
Name - name of the virus, I.E. COVID-19
Long name - name of the virus, I.E. Sars-cov-2
R0 - the average number of people who will contract a contagious disease from one person with that disease

See this site for more info: https://www.healthline.com/health/r-nought-reproduction-number
mortality rate- https://www.worldometers.info/coronavirus/coronavirus-death-rate/

# Init method:
takes in Name, Long name, R0, and mortality rate and sets them as private attributes

# Getter Methods:
get_name: gets the private attribute name
get_long_name: gets the private attribute long name
get_r0(): gets the private attribute r0
get_mortality_rate(): gets the private attribute mortality rate --> -->

# First Assignement:

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

# Additional exercise - Inserting multiple viruses, and creating a time series
Using the data Josh created in the event_cards.json data, I extended the vires.json file for as many viruses that are in city.json. (see below) Since all of these are area_affected = 'federal', and are event_type = 'mutation', you can apply the changes to any event_card that is applied_federally. In the apply_federally defined function, if the event_type = 'mutation', you can then search for the matching virus, and apply the mortality_rate, and r0 to the affected areas using a method of the EventCard class.

The next step is to create a time series. A time series is a plot of how the data changes over time. In order to do this, we need to capture the data, and save it each week after the event_cards are applied to their affected areas. Since the data in our list of cites is all pointed to the current values, this is not as simple as just appending to a list each iteration. Instead, I created a list of dictionaries, to hold the lists of the changes as they occur. (see example below) After each event_card is applied, I would save the current data to the Dictionary for each affectd city. I added a list to each city dictionary for the time series data called 'week'. This list could easy just be the string of integers from our week count iterations, and you can easily graph and attribute against it. I used pandas to creat a time series so the week lists have actual date formatted data to plot against, and appended this date for each iteration.

Once all the data is collected, you can create a plot of any city showing how any of its attributes changed over time. Matplotlib has a plot_date() function that make this super easy.

Here is the dictionary for Phoenix after 5 weeks, plus the starting values:

{'deaths': [0, 0, 0, 0, 55159.16, 55159.16],
 'infected_population': [0, 884476, 160814, 418116, 787988, 948802],
 'name': 'Phoenix',
 'open_hires': [0, 118841, 118841, -5628, 36826, 36826],
 'population': 1608139,
 'r0': [0.96, 1.34, 0.89, 1.16, 2.0, 1.55],
 'unemployment_rate': [0, 7.39, 2.79, -0.35, 2.29, 2.29],
 'week': [datetime.date(2022, 9, 7),
          datetime.date(2022, 9, 11),
          datetime.date(2022, 9, 18),
          datetime.date(2022, 9, 25),
          datetime.date(2022, 10, 2),
          datetime.date(2022, 10, 16)]}

Here is the virus.json:

[
    {
      "name": "Omicron",
      "long_name": "SARS COVID19 Omicron",
      "r0": 1.9,
      "mortality_rate" : 0.08
    },
    {
      "name": "Alpha",
      "long_name": "SARS COVID19 Alpha",
      "r0": 0.9,
      "mortality_rate" : 0.07
    },
    {
      "name": "Beta",
      "long_name": "SARS COVID19 Beta",
      "r0": 0.8,
      "mortality_rate" : 0.07
    },
    {
      "name": "Delta",
      "long_name": "SARS COVID19 Delta",
      "r0": 2.0,
      "mortality_rate" : 0.07
    },
    {
      "name": "Gamma",
      "long_name": "SARS COVID10 Gamma",
      "r0": 1.1,
      "mortality_rate" : 0.088
    },
    {
      "name": "Iota",
      "long_name": "SARS COVID19 Iota",
      "r0": 1.2,
      "mortality_rate" : 0.075
    },
    {
      "name": "Kappa",
      "long_name": "SARS COVID10 Kappa",
      "r0": 1.6,
      "mortality_rate" : 0.045
    },
    {
      "name": "Zeta",
      "long_name": "SARS COVID10 Zeta",
      "r0": 1.3,
      "mortality_rate" : 0.0835
    }
]




