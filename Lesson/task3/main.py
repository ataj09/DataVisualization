import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# TODO: Create a bar plot of total global sales by platform
def plot_total_global_sales_by_platform(df):

    sns.barplot(x='platform', y='global_sales', data=df, estimator=sum, ci=None)
    plt.title('Total Global Sales by Platform')
    plt.xlabel('Platform')
    plt.ylabel('Total Global Sales (in millions)')
    plt.xticks(rotation=45)
    plt.show()

# TODO: Create a histogram of global sales
def plot_distribution_of_global_sales(df):
    sns.histplot(df['global_sales'], bins=30, kde=True)
    plt.title('Distribution of Global Sales')
    plt.xlabel('Global Sales (in millions)')
    plt.show()

 # TODO: Create a scatter plot of global sales vs. critic score
def plot_global_sales_vs_critic_score(df):

    sns.scatterplot(x='critic_score', y='global_sales', data=df)
    plt.title('Global Sales vs. Critic Score')
    plt.xlabel('Critic Score')
    plt.ylabel('Global Sales (in millions)')
    plt.show()
