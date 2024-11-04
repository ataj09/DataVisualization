import unittest
from io import StringIO
from unittest.mock import patch
from main import (
    select_names,
    select_name_and_platform,
    select_first_row,
    select_row_by_name,
    get_second_game_platform,
    filter_sales_above_10,
    filter_sales_and_platform,
    filter_by_platforms,
    add_myscore_column,
    modify_global_sales,
    drop_critic_count_column,
    drop_first_row
)
import pandas as pd
import os

class TestCase(unittest.TestCase):
    def setUp(self):
        self.file_path = '../../common/dataset.csv'
        self.df = pd.read_csv(self.file_path)

    def test_select_names(self):
        # Test if select_names function returns the correct column
        names = select_names(self.df)
        self.assertEqual(names.name, 'name')  # Verify that the Series is named 'name'
        self.assertEqual(len(names), len(self.df))  # Check length matches original DataFrame

    def test_select_name_and_platform(self):
        # Test if select_name_and_platform returns correct DataFrame structure
        selected_df = select_name_and_platform(self.df)
        self.assertIn('name', selected_df.columns)
        self.assertIn('platform', selected_df.columns)
        self.assertEqual(len(selected_df.columns), 2)

    def test_select_first_row(self):
        # Test if select_first_row returns the first row of the DataFrame
        first_row = select_first_row(self.df)
        expected_row = self.df.iloc[0]
        pd.testing.assert_series_equal(first_row, expected_row)

    def test_select_row_by_name(self):
        # Test if select_row_by_name retrieves the correct row
        row = select_row_by_name(self.df, 'Destiny')
        expected_row = self.df.loc[self.df['name'] == 'Destiny']
        pd.testing.assert_frame_equal(row, expected_row)

    def test_get_second_game_platform(self):
        # Test if get_second_game_platform returns the correct platform
        platform = get_second_game_platform(self.df)
        second_game_name = self.df.iloc[1]['name']
        expected_platform = self.df.loc[self.df['name'] == second_game_name, 'platform'].values[0]
        self.assertEqual(platform, expected_platform)

    def test_filter_sales_above_10(self):
        # Test if filter_sales_above_10 returns correct rows
        filtered_df = filter_sales_above_10(self.df)
        self.assertTrue((filtered_df['global_sales'] > 10).all())  # All values should be > 10

    def test_filter_sales_and_platform(self):
        # Test if filter_sales_and_platform returns correct rows
        filtered_df = filter_sales_and_platform(self.df)
        self.assertTrue((filtered_df['global_sales'] > 10).all())
        self.assertTrue((filtered_df['platform'] == 'PS4').all())

    def test_filter_by_platforms(self):
        # Test if filter_by_platforms returns correct rows
        filtered_df = filter_by_platforms(self.df)
        self.assertTrue(filtered_df['platform'].isin(['PS4', 'XOne']).all())

    def test_add_myscore_column(self):
        # Test if add_myscore_column adds a new column correctly
        modified_df = add_myscore_column(self.df)
        self.assertIn('myscore', modified_df.columns)
        self.assertTrue((modified_df['myscore'] == 2).all())  # Check if all values are 2

    def test_modify_global_sales(self):
        # Test if modify_global_sales increments global_sales correctly
        original_sales = self.df['global_sales'].copy()
        modified_df = modify_global_sales(self.df)
        self.assertTrue((modified_df['global_sales'] == original_sales + 1).all())  # Verify the increment

    def test_drop_critic_count_column(self):
        # Test if drop_critic_count_column removes the critic_count column
        modified_df = drop_critic_count_column(self.df)
        self.assertNotIn('critic_count', modified_df.columns)  # Check if the column is removed

    def test_drop_first_row(self):
        # Test if drop_first_row removes the first row correctly
        modified_df = drop_first_row(self.df)
        self.assertNotEqual(len(modified_df), len(self.df))  # Length should be reduced by 1
        self.assertTrue((modified_df.index != self.df.index[0]).all())  # Ensure first row is dropped

