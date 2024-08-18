import pytest
import faker_usage

def test_blood_group_value_tuples():
    assert faker_usage.calculate_statistics_with_named_tuples(10_000)[0] in {'A', 'B', 'O', 'A+', 'B+', 'O+', 'A-', 'B-', 'O-', 'AB+'}


def test_lat_value_tuples():
    assert -90<= faker_usage.calculate_statistics_with_named_tuples(10_000)[1] <= 90

def test_long_value_tuples():
    assert -180<= faker_usage.calculate_statistics_with_named_tuples(10_000)[2] <= 180

def test_oldest_age_value_tuples():
    assert 0<= faker_usage.calculate_statistics_with_named_tuples(10_000)[3] <= 150

def test_average_age_value_tuples():
    assert 0<= faker_usage.calculate_statistics_with_named_tuples(10_000)[4] <= 150

def test_blood_group_value_dict():
    assert faker_usage.calculate_statistics_with_dict(10_000)[0] in {'A', 'B', 'O', 'A+', 'B+', 'O+', 'A-', 'B-', 'O-', 'AB+'}


def test_lat_value_dict():
    assert -90<= faker_usage.calculate_statistics_with_dict(10_000)[1] <= 90

def test_long_value_dict():
    assert -180<= faker_usage.calculate_statistics_with_dict(10_000)[2] <= 180

def test_oldest_age_value_dict():
    assert 0<= faker_usage.calculate_statistics_with_dict(10_000)[3] <= 150

def test_average_age_value_dict():
    assert 0<= faker_usage.calculate_statistics_with_dict(10_000)[4] <= 150


def test_close_stock():
    out = faker_usage.calculate_stock_market_statistics(100)
    assert out[0] <= out[2] <= out[1]

def test_negative_count_stock():
    with pytest.raises(ValueError):
        faker_usage.calculate_stock_market_statistics(-100)

def test_stock_open_value():
    assert faker_usage.calculate_stock_market_statistics(100)[0] > 0

def test_stock_high_value():
    assert faker_usage.calculate_stock_market_statistics(100)[1] > 0

def test_stock_close_value():
    assert faker_usage.calculate_stock_market_statistics(100)[2] > 0