from faker import Faker
from typing import Tuple, List
import random
import time
from collections import namedtuple, Counter
from datetime import datetime
from operator import itemgetter

Faker.seed(121)

def get_random_profiles(count_profiles: int, required_fields: List) -> List:
    """Generates random profiles using faker package

    Args:
        count_profiles (int): integer value mentioning count of profiles to generate
        required_fields (List): list of strings mentioning required profile features

    Raises:
        ValueError: If count_profiles non positive raises value error

    Returns:
        List: returns list of profiles 
    """
    if count_profiles <= 0:
        raise ValueError("count_profiles should be a positive number")
    fake = Faker()
    return [dict(zip(required_fields, itemgetter(*required_fields)(fake.profile()))) for _ in range(count_profiles)]

def calculate_statistics_with_named_tuples(profile_list: List) -> Tuple:
    """Calculate aggregate statistis for passed profiles

    Args:
        profile_list (List): list profiles

    Returns:
        Tuple: returns a named tuple containing all desired statistics using tuple data structure
    """
    if not profile_list:
        raise ValueError("profile_list should not be empty")
    
    if any([len({'blood_group', 'current_location', 'birthdate'}.difference(set(p.keys()))) != 0 for p in profile_list]):
        raise ValueError("Each profile must contain the keys: {'birthdate', 'current_location', 'blood_group'}")

    
    count_profiles = len(profile_list)
    Profile = namedtuple('Profile', profile_list[0].keys())
    profile_list = [Profile(**profile) for profile in profile_list]

    largest_blood_group = Counter([p.blood_group for p in profile_list]).most_common(1)[0][0]
    mean_lat = sum((p.current_location[0] for p in profile_list))/count_profiles
    mean_long = sum((p.current_location[1] for p in profile_list))/count_profiles
    oldest_age = max(((datetime.now().date() - p.birthdate).days/365 for p in profile_list))
    avg_age = sum(((datetime.now().date() - p.birthdate).days/365 for p in profile_list))/count_profiles
    return namedtuple('Statistics', 'largest_blood_group mean_lat mean_long oldest_age avg_age')(largest_blood_group, mean_lat, mean_long, oldest_age, avg_age)


def calculate_statistics_with_dict(profile_list: List) -> Tuple:
    """Calculate aggregate statistis for passed profiles

    Args:
        profile_list (List): list profiles

    Returns:
        Tuple: returns a named tuple containing all desired statistics using dict data structure
    """
    if not profile_list:
        raise ValueError("profile_list should not be empty")
    
    if any([len({'blood_group', 'current_location', 'birthdate'}.difference(set(p.keys()))) != 0 for p in profile_list]):
        raise ValueError("Each profile must contain the keys: {'birthdate', 'current_location', 'blood_group'}")

    count_profiles = len(profile_list)

    largest_blood_group = Counter([p['blood_group'] for p in profile_list]).most_common(1)[0][0]
    mean_lat = sum((p['current_location'][0] for p in profile_list))/count_profiles
    mean_long = sum((p['current_location'][1] for p in profile_list))/count_profiles
    oldest_age = max(((datetime.now().date() - p['birthdate']).days/365 for p in profile_list))
    avg_age = sum(((datetime.now().date() - p['birthdate']).days/365 for p in profile_list))/count_profiles
    return namedtuple('Statistics', 'largest_blood_group mean_lat mean_long oldest_age avg_age')(largest_blood_group, mean_lat, mean_long, oldest_age, avg_age)


def get_random_companies(count_companies: int) -> Tuple:
    """Get random stock market companies

    Args:
        count_companies (int): count of companies to generate

    Raises:
        ValueError: raise value error when count_companies is non positive

    Returns:
        Tuple: return a named tuple containing stock market data
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

    return company_list

def calculate_stock_market_statistics(companies_list: List) -> Tuple:
    """Calculate stock market statistics from passed set of companies

    Args:
        companies_list (List): list of companies to consider

    Returns:
        Tuple: return a named tuple consisting all the statistics of stock market
    """
    if sum((p.weight for p in companies_list)) == 0:
        raise ZeroDivisionError("Weights sum cannot be zero")
    
    if any(p.weight < 0 for p in companies_list):
        raise ValueError("Weight should be a positive number")
    stock_mkt_open = sum((p.open*p.weight for p in companies_list))/sum((p.weight for p in companies_list))
    stock_mkt_high = sum((p.high*p.weight for p in companies_list))/sum((p.weight for p in companies_list))
    stock_mkt_close = sum((p.close*p.weight for p in companies_list))/sum((p.weight for p in companies_list))

    return namedtuple('Statistics', 'stock_mkt_open stock_mkt_high stock_mkt_close')(stock_mkt_open, stock_mkt_high, stock_mkt_close)
