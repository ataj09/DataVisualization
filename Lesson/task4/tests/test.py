import unittest
import pandas as pd
import matplotlib.pyplot as plt
from main import get_grouped, plot_final_task

class TestFinalTask(unittest.TestCase):
    def setUp(self):
        self.file_path = '../../common/dataset.csv'
        self.df = pd.read_csv(self.file_path)

    def test_get_grouped(self):

        self.df = self.df[self.df['platform'].isin(['PS4', 'XOne', 'PC', 'WiiU'])]
        result = get_grouped(self.df)
        expected_values = self.df.groupby(['platform', 'genre']).size().reset_index(name='count')

        pd.testing.assert_frame_equal(result, expected_values)
        self.assertListEqual(list(result.columns), ['platform', 'genre', 'count'])


    def test_plot_games_per_genre_grouped_by_platform_correct_values(self):

        df = self.df[self.df['platform'].isin(['PS4', 'XOne', 'PC', 'WiiU'])]
        platform_genre_counts = get_grouped(df)
        plot_final_task(platform_genre_counts)
        ax = plt.gca()
        bars = ax.patches
        for bar, (_, row) in zip(bars, platform_genre_counts.iterrows()):
            expected_count = row['count']
            actual_count = bar.get_height()
            self.assertEqual(actual_count, expected_count)
        plt.close()