import pytest
import faker_usage
from collections import namedtuple

import unittest
from datetime import datetime
from faker_usage import calculate_statistics_with_named_tuples, calculate_statistics_with_dict, calculate_stock_market_statistics

class TestCalculateStatisticsWithNamedTuples(unittest.TestCase):

    def setUp(self):
        """Set up common test data"""
        self.current_date = datetime.now().date()
        self.profile_list_valid = [
            {
                'blood_group': 'O+',
                'current_location': (40.7128, -74.0060),
                'birthdate': self.current_date.replace(year=self.current_date.year - 25)
            },
            {
                'blood_group': 'A+',
                'current_location': (34.0522, -118.2437),
                'birthdate': self.current_date.replace(year=self.current_date.year - 30)
            },
            {
                'blood_group': 'O+',
                'current_location': (37.7749, -122.4194),
                'birthdate': self.current_date.replace(year=self.current_date.year - 40)
            }
        ]

    def test_valid_profiles_tuple(self):
        """Test with a valid list of profiles"""
        result = calculate_statistics_with_named_tuples(self.profile_list_valid)
        self.assertEqual(result.largest_blood_group, 'O+')
        self.assertAlmostEqual(result.mean_lat, (40.7128 + 34.0522 + 37.7749) / 3)
        self.assertAlmostEqual(result.mean_long, (-74.0060 - 118.2437 - 122.4194) / 3)
        self.assertAlmostEqual(result.oldest_age, 40, 0)
        self.assertAlmostEqual(result.avg_age, (25 + 30 + 40) / 3, 0)

    def test_empty_profile_list_tuple(self):
        """Test with an empty list of profiles"""
        with self.assertRaises(ValueError) as context:
            calculate_statistics_with_named_tuples([])
        self.assertEqual(str(context.exception), "profile_list should not be empty")

    def test_missing_fields_tuple(self):
        """Test with profiles missing required fields"""
        invalid_profiles = [
            {
                'blood_group': 'O+',
                'current_location': (40.7128, -74.0060)
                # 'birthdate' is missing
            }
        ]
        with self.assertRaises(ValueError) as context:
            calculate_statistics_with_named_tuples(invalid_profiles)
        self.assertEqual(str(context.exception), "Each profile must contain the keys: {'birthdate', 'current_location', 'blood_group'}")

    def test_profiles_with_identical_data_tuple(self):
        """Test with profiles having identical data"""
        identical_profiles = [
            {
                'blood_group': 'B+',
                'current_location': (50.0000, -100.0000),
                'birthdate': self.current_date.replace(year=self.current_date.year - 30)
            },
            {
                'blood_group': 'B+',
                'current_location': (50.0000, -100.0000),
                'birthdate': self.current_date.replace(year=self.current_date.year - 30)
            }
        ]
        result = calculate_statistics_with_named_tuples(identical_profiles)
        self.assertEqual(result.largest_blood_group, 'B+')
        self.assertEqual(result.mean_lat, 50.0000)
        self.assertEqual(result.mean_long, -100.0000)
        self.assertAlmostEqual(result.oldest_age, 30, 0)
        self.assertAlmostEqual(result.avg_age, 30, 0)

    def test_single_profile_tuple(self):
        """Test with a single profile"""
        single_profile = [
            {
                'blood_group': 'AB+',
                'current_location': (55.7558, 37.6176),
                'birthdate': self.current_date.replace(year=self.current_date.year - 22)
            }
        ]
        result = calculate_statistics_with_named_tuples(single_profile)
        self.assertEqual(result.largest_blood_group, 'AB+')
        self.assertEqual(result.mean_lat, 55.7558)
        self.assertEqual(result.mean_long, 37.6176)
        self.assertAlmostEqual(result.oldest_age, 22, 0)
        self.assertAlmostEqual(result.avg_age, 22, 0)

    def test_valid_profiles_dict(self):
        """Test with a valid list of profiles"""
        result = calculate_statistics_with_dict(self.profile_list_valid)
        self.assertEqual(result.largest_blood_group, 'O+')
        self.assertAlmostEqual(result.mean_lat, (40.7128 + 34.0522 + 37.7749) / 3)
        self.assertAlmostEqual(result.mean_long, (-74.0060 - 118.2437 - 122.4194) / 3)
        self.assertAlmostEqual(result.oldest_age, 40, 0)
        self.assertAlmostEqual(result.avg_age, (25 + 30 + 40) / 3, 0)

    def test_empty_profile_list_dict(self):
        """Test with an empty list of profiles"""
        with self.assertRaises(ValueError) as context:
            calculate_statistics_with_dict([])
        self.assertEqual(str(context.exception), "profile_list should not be empty")

    def test_missing_fields_dict(self):
        """Test with profiles missing required fields"""
        invalid_profiles = [
            {
                'blood_group': 'O+',
                'current_location': (40.7128, -74.0060)
                # 'birthdate' is missing
            }
        ]
        with self.assertRaises(ValueError) as context:
            calculate_statistics_with_dict(invalid_profiles)
        self.assertEqual(str(context.exception), "Each profile must contain the keys: {'birthdate', 'current_location', 'blood_group'}")

    def test_profiles_with_identical_data_dict(self):
        """Test with profiles having identical data"""
        identical_profiles = [
            {
                'blood_group': 'B+',
                'current_location': (50.0000, -100.0000),
                'birthdate': self.current_date.replace(year=self.current_date.year - 30)
            },
            {
                'blood_group': 'B+',
                'current_location': (50.0000, -100.0000),
                'birthdate': self.current_date.replace(year=self.current_date.year - 30)
            }
        ]
        result = calculate_statistics_with_dict(identical_profiles)
        self.assertEqual(result.largest_blood_group, 'B+')
        self.assertEqual(result.mean_lat, 50.0000)
        self.assertEqual(result.mean_long, -100.0000)
        self.assertAlmostEqual(result.oldest_age, 30, 0)
        self.assertAlmostEqual(result.avg_age, 30, 0)

    def test_single_profile_dict(self):
        """Test with a single profile"""
        single_profile = [
            {
                'blood_group': 'AB+',
                'current_location': (55.7558, 37.6176),
                'birthdate': self.current_date.replace(year=self.current_date.year - 22)
            }
        ]
        result = calculate_statistics_with_dict(single_profile)
        self.assertEqual(result.largest_blood_group, 'AB+')
        self.assertEqual(result.mean_lat, 55.7558)
        self.assertEqual(result.mean_long, 37.6176)
        self.assertAlmostEqual(result.oldest_age, 22, 0)
        self.assertAlmostEqual(result.avg_age, 22, 0)


class TestCalculateStockMarketStatistics(unittest.TestCase):

    def setUp(self):
        """Set up common test data"""
        self.Company = namedtuple('Company', 'company_name symbol open high close weight')

        # Valid list of companies
        self.company_list_valid = [
            self.Company(company_name='Company A', symbol='ABC', open=150, high=200, close=180, weight=0.5),
            self.Company(company_name='Company B', symbol='XYZ', open=120, high=170, close=140, weight=0.5)
        ]

        # List with zero weight
        self.company_list_zero_weight = [
            self.Company(company_name='Company C', symbol='DEF', open=180, high=220, close=200, weight=0.0),
            self.Company(company_name='Company D', symbol='GHI', open=140, high=190, close=160, weight=1.0)
        ]

        # List with a single company
        self.company_list_single = [
            self.Company(company_name='Company E', symbol='JKL', open=200, high=250, close=230, weight=1.0)
        ]

        # List with negative weight
        self.company_list_negative_weight = [
            self.Company(company_name='Company F', symbol='MNO', open=150, high=200, close=180, weight=-0.5),
            self.Company(company_name='Company G', symbol='PQR', open=100, high=150, close=120, weight=-0.5)
        ]

        # List with identical values
        self.company_list_identical = [
            self.Company(company_name='Company H', symbol='STU', open=150, high=200, close=180, weight=0.33),
            self.Company(company_name='Company I', symbol='VWX', open=150, high=200, close=180, weight=0.33),
            self.Company(company_name='Company J', symbol='YZA', open=150, high=200, close=180, weight=0.34)
        ]

        # List with only one company with zero weight
        self.company_list_zero_weight_single = [
            self.Company(company_name='Company K', symbol='BCD', open=200, high=250, close=230, weight=0.0)
        ]

        # Empty list
        self.company_list_empty = []

        # List with weight summing to zero
        self.company_list_weight_zero_sum = [
            self.Company(company_name='Company L', symbol='EFG', open=100, high=150, close=120, weight=0.5),
            self.Company(company_name='Company M', symbol='HIJ', open=120, high=170, close=140, weight=-0.5)
        ]

        # Very large weights
        self.company_list_large_weights = [
            self.Company(company_name='Company N', symbol='KLM', open=100, high=150, close=120, weight=1e6),
            self.Company(company_name='Company O', symbol='NOP', open=120, high=170, close=140, weight=1e6)
        ]

        # Very small weights
        self.company_list_small_weights = [
            self.Company(company_name='Company P', symbol='QRS', open=100, high=150, close=120, weight=1e-6),
            self.Company(company_name='Company Q', symbol='TUV', open=120, high=170, close=140, weight=1e-6)
        ]

    def test_valid_company_list(self):
        """Test with a valid list of companies"""
        result = calculate_stock_market_statistics(self.company_list_valid)
        weighted_open = (150 * 0.5 + 120 * 0.5) / (0.5 + 0.5)
        weighted_high = (200 * 0.5 + 170 * 0.5) / (0.5 + 0.5)
        weighted_close = (180 * 0.5 + 140 * 0.5) / (0.5 + 0.5)
        self.assertAlmostEqual(result.stock_mkt_open, weighted_open)
        self.assertAlmostEqual(result.stock_mkt_high, weighted_high)
        self.assertAlmostEqual(result.stock_mkt_close, weighted_close)

    def test_zero_weight(self):
        """Test with companies that have zero weight"""
        result = calculate_stock_market_statistics(self.company_list_zero_weight)
        weighted_open = 140  # Only the non-zero weight company should be considered
        weighted_high = 190
        weighted_close = 160
        self.assertAlmostEqual(result.stock_mkt_open, weighted_open)
        self.assertAlmostEqual(result.stock_mkt_high, weighted_high)
        self.assertAlmostEqual(result.stock_mkt_close, weighted_close)

    def test_single_company(self):
        """Test with a single company in the list"""
        result = calculate_stock_market_statistics(self.company_list_single)
        self.assertEqual(result.stock_mkt_open, 200)
        self.assertEqual(result.stock_mkt_high, 250)
        self.assertEqual(result.stock_mkt_close, 230)

    def test_negative_weight(self):
        """Test with companies having negative weights"""
        with self.assertRaises(ValueError):
            calculate_stock_market_statistics(self.company_list_negative_weight)

    def test_identical_values(self):
        """Test with companies having identical values"""
        result = calculate_stock_market_statistics(self.company_list_identical)
        self.assertEqual(result.stock_mkt_open, 150)
        self.assertEqual(result.stock_mkt_high, 200)
        self.assertEqual(result.stock_mkt_close, 180)

    def test_zero_weight_single_company(self):
        """Test with a single company having zero weight"""
        with self.assertRaises(ZeroDivisionError):
            calculate_stock_market_statistics(self.company_list_zero_weight_single)

    def test_empty_list(self):
        """Test with an empty list of companies"""
        with self.assertRaises(ZeroDivisionError):
            calculate_stock_market_statistics(self.company_list_empty)

    def test_weight_sum_zero(self):
        """Test with companies where weights sum to zero"""
        with self.assertRaises(ZeroDivisionError):
            calculate_stock_market_statistics(self.company_list_weight_zero_sum)

    def test_large_weights(self):
        """Test with very large weights"""
        result = calculate_stock_market_statistics(self.company_list_large_weights)
        weighted_open = (100 * 1e6 + 120 * 1e6) / (1e6 + 1e6)
        weighted_high = (150 * 1e6 + 170 * 1e6) / (1e6 + 1e6)
        weighted_close = (120 * 1e6 + 140 * 1e6) / (1e6 + 1e6)
        self.assertAlmostEqual(result.stock_mkt_open, weighted_open)
        self.assertAlmostEqual(result.stock_mkt_high, weighted_high)
        self.assertAlmostEqual(result.stock_mkt_close, weighted_close)

    def test_small_weights(self):
        """Test with very small weights"""
        result = calculate_stock_market_statistics(self.company_list_small_weights)
        weighted_open = (100 * 1e-6 + 120 * 1e-6) / (1e-6 + 1e-6)
        weighted_high = (150 * 1e-6 + 170 * 1e-6) / (1e-6 + 1e-6)
        weighted_close = (120 * 1e-6 + 140 * 1e-6) / (1e-6 + 1e-6)
        self.assertAlmostEqual(result.stock_mkt_open, weighted_open)
        self.assertAlmostEqual(result.stock_mkt_high, weighted_high)
        self.assertAlmostEqual(result.stock_mkt_close, weighted_close)