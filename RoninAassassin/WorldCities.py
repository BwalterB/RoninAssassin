import pandas as pd
import random as r

Country = []
#QUESTION
#how to pull in live data from a global weather service that will show weather in that city as it currently is

countries = pd.read_csv('RoninAssassin\RoninAassassin\Top100PopulatedCitiesAndDrinks.csv')
#print(text)

World_Cities = []

for i in countries["Country"]:
    Country.append(i)

for p in countries["City"]:
    World_Cities.append(p)

city_of_operation = r.choice(World_Cities)

#print(Country)
print(World_Cities)

#print(type(countries))