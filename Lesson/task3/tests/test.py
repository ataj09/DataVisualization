import unittest
from io import StringIO
from unittest.mock import patch
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from main import plot_total_global_sales_by_platform, plot_distribution_of_global_sales, plot_global_sales_vs_critic_score

class TestVisualizationFunctions(unittest.TestCase):
    def setUp(self):
        self.file_path = '../../common/dataset.csv'
        self.df = pd.read_csv(self.file_path)

    @patch('matplotlib.pyplot.show')
    def test_plot_total_global_sales_by_platform(self, mock_show):
        plot_total_global_sales_by_platform(self.df)
        mock_show.assert_called_once()

    @patch('matplotlib.pyplot.show')
    def test_plot_distribution_of_global_sales(self, mock_show):
        plot_distribution_of_global_sales(self.df)
        mock_show.assert_called_once()

    @patch('matplotlib.pyplot.show')
    def test_plot_global_sales_vs_critic_score(self, mock_show):
        plot_global_sales_vs_critic_score(self.df)
        mock_show.assert_called_once()
