#!/usr/bin/env python


import csv
import numpy as np
import pandas as pd
import scipy.stats as stats
from datetime import datetime
from datetime import timedelta

## load data
df_people = pd.read_csv("people-data.csv")

def generate_person(fm_ratio=0.5):
    """
    generate a new person using df_people
    """
    
    print(list(df_people.columns))


def random_day(start, end):
    """
    return a random datetime between two datetimes 
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def get_birthday(age):
    """
    return a random birthday given an age
    """

    today = datetime.now()
    birthday = today - timedelta(days=(365*age) + np.random.randint(-180,180))

    ## sainity check
    if np.abs((today-birthday).days-(365*age)) > 365:
        raise exception("generated a birthday that was not possible",birthday,age)

    #print(today,birthday,days_from)

    return(birthday)

def generate_people(n,fm_ratio=0.5):
    """
    n: number of people to generate
    fm_ratio: 0-1 female to male ratio
    """

    if n > 1000:
        raise Exception("script only works with max of n=1000.. run multiple times and concat")

    ## gender specific variables
    genders = np.random.binomial(n=1,p=fm_ratio,size=n)
    female_indices = np.where(genders==1)[0]
    male_indices = np.where(genders==0)[0]
    print('...generating {} males'.format(male_indices.size))
    print('...generating {} females'.format(female_indices.size))
    
    ## determin the first names
    possible_female_first_names = df_people['female_first'].values
    possible_female_first_names = np.random.permutation(possible_female_first_names)
    possible_male_first_names = df_people['male_first'].values
    possible_male_first_names = np.random.permutation(possible_male_first_names)

    first_names = np.empty(n,dtype=np.chararray)
    first_names[female_indices] = possible_female_first_names[:female_indices.size]
    first_names[male_indices] = possible_male_first_names[:male_indices.size]

    ## determine the last names
    possible_last_names = df_people['common_last'].values
    possible_last_names = np.random.permutation(possible_last_names)
    last_names = [lname.capitalize() for lname in possible_last_names[:n]]
    
    ## determin ages  (two component gaussian)
    modes = np.random.binomial(n=1,p=0.3,size=n)
    mode1 = np.where(modes==0)[0]
    mode2 = np.where(modes==1)[0]
    ages = np.zeros(n)
    ages[mode1] = stats.norm(loc=22,scale=3).rvs(mode1.size)
    ages[mode2] = stats.norm(loc=40,scale=6).rvs(mode2.size)
    ages = [int(round(age)) for age in ages]


    ## make up some birthdays from the known age    
    dobs = [get_birthday(age).strftime("%x") for age in ages]

    ## get the city, state and country
    rand_order = np.random.permutation(np.arange(n))
    possible_cities = df_people['city'].values
    possible_cities = possible_cities[rand_order]
    possible_states = df_people['state'].values
    possible_states = possible_states[rand_order]
    
    cities = possible_cities[:n]
    states = possible_states[:n]
    countries = np.empty(n,dtype=np.chararray)
    countries[:] = "united_states"

    ## modify the locations to be 1/3 from singapore
    rand_inds = np.random.permutation(np.arange(n))[:int(round(0.3*n))]
    countries[rand_inds] = "singapore"
    cities[rand_inds] = "singapore"
    states[rand_inds] = ""

    header = ["last_name","first_name","gender","age","dob_(mm/dd/yy)","city","state","country"]
    genders = ['m' if g == 0 else 'f' for g in genders]
    with open('people-out.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for i in range(n):
            writer.writerow([last_names[i], first_names[i], genders[i], ages[i], dobs[i], cities[i], states[i], countries[i]])

    print("done")
    

if __name__ == "__main__":

    np.random.seed(42)
    fm_ratio = 0.4
    generate_people(n=1000,fm_ratio=fm_ratio)
