from faker import Faker
from typing import Tuple
import random
import time
from collections import namedtuple, Counter
from datetime import datetime
from operator import itemgetter

Faker.seed(121)

def calculate_statistics_with_named_tuples(count_profiles: int) -> Tuple:
    """Calculate aggregate statistis for fake generated profiles

    Args:
        count_profiles (int): Number of profiles to generate

    Returns:
        Tuple: Aggregate statistics calculated on fake profiles.It has following metrics:
        largest_blood_group, mean_lat, mean_long, oldest_age, avg_age
    """
    if count_profiles <= 0:
        raise ValueError("count_profiles should be a positive number")
    
    profile_list = []
    keys = ["blood_group", "current_location", "birthdate"]
    fake = Faker()
    Profile = namedtuple('Profile', keys)
    profile_list = [Profile(**dict(zip(keys, itemgetter(*keys)(fake.profile())))) for _ in range(count_profiles)]

    largest_blood_group = Counter([p.blood_group for p in profile_list]).most_common(1)[0][0]
    mean_lat = sum((p.current_location[0] for p in profile_list))/count_profiles
    mean_long = sum((p.current_location[1] for p in profile_list))/count_profiles
    oldest_age = max(((datetime.now().date() - p.birthdate).days/365 for p in profile_list))
    avg_age = sum(((datetime.now().date() - p.birthdate).days/365 for p in profile_list))/count_profiles
    return namedtuple('Statistics', 'largest_blood_group mean_lat mean_long oldest_age avg_age')(largest_blood_group, mean_lat, mean_long, oldest_age, avg_age)


def calculate_statistics_with_dict(count_profiles: int) -> Tuple:
    """Calculate aggregate statistis for fake generated profiles

    Args:
        count_profiles (int): Number of profiles to generate

    Returns:
        Tuple: Aggregate statistics calculated on fake profiles.It has following metrics:
        largest_blood_group, mean_lat, mean_long, oldest_age, avg_age
    """
    if count_profiles <= 0:
        raise ValueError("count_profiles should be a positive number")
    
    profile_list = []
    fake = Faker()
    profile_list = [fake.profile() for _ in range(count_profiles)]
    
    largest_blood_group = Counter([p['blood_group'] for p in profile_list]).most_common(1)[0][0]
    mean_lat = sum((p['current_location'][0] for p in profile_list))/count_profiles
    mean_long = sum((p['current_location'][1] for p in profile_list))/count_profiles
    oldest_age = max(((datetime.now().date() - p['birthdate']).days/365 for p in profile_list))
    avg_age = sum(((datetime.now().date() - p['birthdate']).days/365 for p in profile_list))/count_profiles
    return namedtuple('Statistics', 'largest_blood_group mean_lat mean_long oldest_age avg_age')(largest_blood_group, mean_lat, mean_long, oldest_age, avg_age)


def calculate_stock_market_statistics(count_companies: int) -> Tuple:
    """Calculate stock market statistics by generating some constituent companies.

    Args:
        count_companies (int): Number of companies to include in the stock market

    Returns:
        Tuple: Returns stock market open, high and close
    """
    if count_companies <= 0:
        raise ValueError("count_companies should be a positive number")
    company_list = []
    fake = Faker()
    Company = namedtuple('Company', 'company_name symbol open high close weight')

    for _ in range(count_companies):
        company_name = fake.company()
        symbol = fake.lexify(text='???', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        open = random.randint(100, 200)
        high = random.randint(open, 230)
        close = random.randint(open, high)
        weight = random.random()
        company_list.append(Company(company_name, symbol, open, high, close, weight))

    stock_mkt_open = sum((p.open*p.weight for p in company_list))/sum((p.weight for p in company_list))
    stock_mkt_high = sum((p.high*p.weight for p in company_list))/sum((p.weight for p in company_list))
    stock_mkt_close = sum((p.close*p.weight for p in company_list))/sum((p.weight for p in company_list))

    return namedtuple('Statistics', 'stock_mkt_open stock_mkt_high stock_mkt_close')(stock_mkt_open, stock_mkt_high, stock_mkt_close)