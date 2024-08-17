from faker import Faker
import random
import time
from collections import namedtuple, Counter
from datetime import datetime
from operator import itemgetter

Faker.seed(121)


def calculate_statistics_with_named_tuples():
    profile_list = []
    keys = ["blood_group", "current_location", "birthdate"]
    fake = Faker()
    Profile = namedtuple('Profile', keys)
    profile_list = [Profile(**dict(zip(keys, itemgetter(*keys)(fake.profile())))) for _ in range(10000)]

    largest_blood_group = Counter([p.blood_group for p in profile_list]).most_common(1)[0][0]
    mean_lat = sum((p.current_location[0] for p in profile_list))/10000
    mean_long = sum((p.current_location[1] for p in profile_list))/10000
    oldest_age = max(((datetime.now().date() - p.birthdate).days/365 for p in profile_list))
    avg_age = sum(((datetime.now().date() - p.birthdate).days/365 for p in profile_list))/10000
    return largest_blood_group, mean_lat, mean_long, oldest_age, avg_age


def calculate_statistics_with_dict():
    profile_list = []
    fake = Faker()
    profile_list = [fake.profile() for _ in range(10000)]
    
    largest_blood_group = Counter([p['blood_group'] for p in profile_list]).most_common(1)[0][0]
    mean_lat = sum((p['current_location'][0] for p in profile_list))/10000
    mean_long = sum((p['current_location'][1] for p in profile_list))/10000
    oldest_age = max(((datetime.now().date() - p['birthdate']).days/365 for p in profile_list))
    avg_age = sum(((datetime.now().date() - p['birthdate']).days/365 for p in profile_list))/10000
    return largest_blood_group, mean_lat, mean_long, oldest_age, avg_age


def calculate_stock_market_statistics():
    company_list = []
    fake = Faker()
    Company = namedtuple('Company', 'company_name symbol open high close weight')

    for _ in range(100):
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

    return stock_mkt_open, stock_mkt_high, stock_mkt_close


  
if __name__ == '__main__':
    start1 = time.perf_counter()
    statistics = calculate_statistics_with_named_tuples()
    print(f"Time taken for tuple data structure: {time.perf_counter() - start1}")
    
    start2 = time.perf_counter()
    statistics = calculate_statistics_with_dict()
    print(f"Time taken for dict data structure: {time.perf_counter() - start1}")

    print(calculate_stock_market_statistics())