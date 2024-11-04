import pandas as pd


# TODO: Return column containing names
def select_names(df):
    return df['name']


# TODO: Return DataFrame with 'name' and 'platform' columns
def select_name_and_platform(df):
    return df[['name', 'platform']]


# TODO: Return the first row of the DataFrame
def select_first_row(df):
    return df.iloc[0]


# TODO: Return row where 'name' matches the given name
def select_row_by_name(df, name='Destiny'):
    return df.loc[df['name'] == name]


# TODO: Return the platform of the second game in the DataFrame
def get_second_game_platform(df):
    second_game_name = df.iloc[1]['name']
    platform = df.loc[df['name'] == second_game_name, 'platform'].values[0]
    return platform


# TODO: Return rows where 'global_sales' is greater than 10
def filter_sales_above_10(df):
    return df[df['global_sales'] > 10]


# TODO: Return rows where 'global_sales' > 10 and 'platform' is 'PS4'
def filter_sales_and_platform(df):
    return df[(df['global_sales'] > 10) & (df['platform'] == 'PS4')]


# TODO: Return rows where 'platform' is either 'PS4' or 'XOne'
def filter_by_platforms(df):
    return df[df['platform'].isin(['PS4', 'XOne'])]


# TODO: Add a new column 'myscore' with a default value
def add_myscore_column(df):
    df['myscore'] = 2
    return df


# TODO: Increase 'global_sales' by 1
def modify_global_sales(df):
    df['global_sales'] = df['global_sales'] + 1
    return df


# TODO: Drop the 'critic_count' column
def drop_critic_count_column(df):
    df = df.drop('critic_count', axis=1, errors='ignore')  # 'errors' param to handle if column doesn't exist
    return df


# TODO: Drop the first row of the DataFrame
def drop_first_row(df):
    df = df.drop(0, axis=0)
    return df

