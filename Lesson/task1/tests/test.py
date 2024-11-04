import unittest
from io import StringIO
from unittest.mock import patch
from main import load_data, df_head, df_tail, df_describe, df_info
import pandas as pd
import os
print(os.getcwd())



class TestCase(unittest.TestCase):
    def setUp(self):
        self.file_path = '../../common/dataset.csv'
        self.df = pd.read_csv(self.file_path)

    def test_load_data(self):

        df = load_data(self.file_path)
        self.assertFalse(df.empty)
        self.assertEqual(len(df.columns), 16)

    def test_df_head(self):
        pd.testing.assert_frame_equal(self.df.head(10), df_head(self.df))

    def test_df_tail(self):
        pd.testing.assert_frame_equal(self.df.tail(5), df_tail(self.df))


    def test_df_describe(self):
        pd.testing.assert_frame_equal(self.df.describe(), df_describe(self.df))

    def test_df_info(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            df_info(self.df)
            self.assertNotEqual(fake_out.getvalue().strip(), "")
