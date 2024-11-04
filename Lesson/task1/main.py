import pandas as pd

# TODO load data into pandas dataframe and return it
def load_data(path_to_file: str) -> pd.DataFrame:
    return pd.read_csv(path_to_file)

# TODO return first 10 rows of dataframe
def df_head(df: pd.DataFrame) -> pd.DataFrame:
    return df.head(10)

# TODO return last 5 rows of dataframe
def df_tail(df: pd.DataFrame) -> pd.DataFrame:
    return df.tail(5)

# TODO display info of dataframe
def df_info(df: pd.DataFrame) -> None:
    print(df.info())

# TODO return numerical analysis of dataframe
def df_describe(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe()
