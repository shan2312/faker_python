# Profile and Stock Market Statistics Calculator

This project provides functions for generating and analyzing random profile data and stock market statistics using the `Faker` library. It includes utilities for creating fake profiles and companies, and calculating various statistics from this generated data.

## Overview

### Functions

1. **`get_random_profiles(count_profiles: int, required_fields: List) -> List`**:
   Generates a specified number of fake profiles using the `Faker` library with the requested fields.

2. **`calculate_statistics_with_named_tuples(profile_list: List) -> Tuple`**:
   Calculates aggregate statistics from a list of profiles represented by named tuples.

3. **`calculate_statistics_with_dict(profile_list: List) -> Tuple`**:
   Calculates aggregate statistics from a list of profiles represented by dictionaries.

4. **`get_random_companies(count_companies: int) -> Tuple`**:
   Generates a specified number of fake stock market companies with random stock data.

5. **`calculate_stock_market_statistics(companies_list: List) -> Tuple`**:
   Calculates stock market statistics from a list of companies, including weighted averages for opening, high, and closing stock prices.

## Requirements

- Python 3.x
- `Faker` library

Install the necessary dependencies with:

```bash
pip install faker
```

## Function Details

### `get_random_profiles`

```python
def get_random_profiles(count_profiles: int, required_fields: List) -> List:
    """
    Generates random profiles using the Faker package.

    Args:
        count_profiles (int): Number of profiles to generate.
        required_fields (List): List of strings specifying the required profile features.

    Raises:
        ValueError: If count_profiles is non-positive.

    Returns:
        List: List of profiles as dictionaries.
    """
```

**Parameters**:
- `count_profiles` (int): The number of profiles to generate. Must be positive.
- `required_fields` (List): List of profile features to include in the generated profiles.

**Returns**:
- `List`: List of dictionaries, each representing a profile with specified features.

### `calculate_statistics_with_named_tuples`

```python
def calculate_statistics_with_named_tuples(profile_list: List) -> Tuple:
    """
    Calculate aggregate statistics for passed profiles using named tuples.

    Args:
        profile_list (List): List of profiles as dictionaries.

    Returns:
        Tuple: Named tuple containing statistics including largest blood group,
               mean latitude, mean longitude, oldest age, and average age.
    """
```

**Parameters**:
- `profile_list` (List): List of profiles as dictionaries.

**Returns**:
- `Tuple`: Named tuple with fields `largest_blood_group`, `mean_lat`, `mean_long`, `oldest_age`, and `avg_age`.

### `calculate_statistics_with_dict`

```python
def calculate_statistics_with_dict(profile_list: List) -> Tuple:
    """
    Calculate aggregate statistics for passed profiles using dictionaries.

    Args:
        profile_list (List): List of profiles as dictionaries.

    Returns:
        Tuple: Named tuple containing statistics including largest blood group,
               mean latitude, mean longitude, oldest age, and average age.
    """
```

**Parameters**:
- `profile_list` (List): List of profiles as dictionaries.

**Returns**:
- `Tuple`: Named tuple with fields `largest_blood_group`, `mean_lat`, `mean_long`, `oldest_age`, and `avg_age`.

### `get_random_companies`

```python
def get_random_companies(count_companies: int) -> Tuple:
    """
    Generate random stock market companies.

    Args:
        count_companies (int): Number of companies to generate.

    Raises:
        ValueError: If count_companies is non-positive.

    Returns:
        Tuple: List of named tuples representing companies with stock data.
    """
```

**Parameters**:
- `count_companies` (int): The number of companies to generate. Must be positive.

**Returns**:
- `Tuple`: List of named tuples, each representing a company with `company_name`, `symbol`, `open`, `high`, `close`, and `weight`.

### `calculate_stock_market_statistics`

```python
def calculate_stock_market_statistics(companies_list: List) -> Tuple:
    """
    Calculate stock market statistics from a list of companies.

    Args:
        companies_list (List): List of companies as named tuples.

    Returns:
        Tuple: Named tuple containing weighted averages for stock market open, high, and close prices.
    """
```

**Parameters**:
- `companies_list` (List): List of companies as named tuples.

**Returns**:
- `Tuple`: Named tuple with fields `stock_mkt_open`, `stock_mkt_high`, and `stock_mkt_close`.

## Usage

Here’s how you can use the functions in your code:

```python
from faker_usage import get_random_profiles, calculate_statistics_with_named_tuples, calculate_statistics_with_dict, get_random_companies, calculate_stock_market_statistics

# Generate random profiles
profiles = get_random_profiles(count_profiles=100, required_fields=['blood_group', 'current_location', 'birthdate'])

# Calculate statistics using named tuples
stats_named_tuples = calculate_statistics_with_named_tuples(profiles)

# Calculate statistics using dictionaries
stats_dict = calculate_statistics_with_dict(profiles)

# Generate random companies
companies = get_random_companies(count_companies=50)

# Calculate stock market statistics
stock_stats = calculate_stock_market_statistics(companies)

print(stats_named_tuples)
print(stats_dict)
print(stock_stats)
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Make sure to include tests and ensure that your code adheres to the project's coding standards.

---
