import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# TODO get number of games per genre grouped by platform
def get_grouped(df: pd.DataFrame) -> pd.DataFrame:
    platform_genre_counts = df.groupby(['platform', 'genre']).size().reset_index(name='count')
    return platform_genre_counts

# TODO plot a bar graph of count of games per genre grouped by platform
def plot_final_task(df: pd.DataFrame):
    plt.figure(figsize=(12, 6))
    sns.barplot(x='platform', y='count', hue='genre', data=df)
    plt.title('count of games per genre grouped by platform')
    plt.xlabel('platform')
    plt.ylabel('number of names')
    plt.xticks(rotation=45)
    plt.show()