# Working with DataFrames in Pandas

In the previous section, we introduced Pandas, discussed its main data structure, 
the DataFrame, and reviewed how to load data from a CSV file. 
Now, let’s dive deeper into DataFrames and learn how to manipulate and retrieve 
data effectively. Mastering these DataFrame operations will allow you to analyze data
more efficiently. 

### Selecting Data in DataFrames

DataFrames allow you to easily access specific columns and rows.

**Selecting Columns**

To select a single column, use square brackets with the column name. This returns a Series (a single-column data structure).

Example:
```python
names = df['name']
print(names)
```

To select multiple columns, pass a list of column names. This will return another DataFrame.

Example:
```python
name_and_platform = df[['name', 'platform']]
print(name_and_platform)
```


**Selecting Rows**:

You can access rows using:
- iloc: For row selection by index.
- loc: For row selection by labels.

Example:
```python
first_row = df.iloc[0]
print(first_row)

alice_row = df.loc[df['name'] == 'Destiny']
print(alice_row)
```


### Accessing Specific Values

For direct access to specific values within a DataFrame, combine loc or iloc with column selection.

Example:
```python
second_game = df.iloc[1]['name']
print(second_game)

game_platform = df.loc[df['name'] == second_game, 'platform'].values[0]
print(bob_age)
```


### Filtering Data with Conditions

Filtering lets you retrieve only the rows that meet specific criteria.

**Basic Filtering**:

Example:
```python
sales_above_10 = df[df['global_sales'] > 10]
print(sales_above_10)
```


**Combining Conditions**:

You can combine conditions with & (and) or | (or).

Example:
```python
filtered_data = df[(df['global_sales'] > 10) & (df['platform'] == 'PS4')]
print(filtered_data)
```

**Using isin to Filter by Multiple Values**:

The isin function is helpful for filtering by multiple values in a column.

Example:
```python
selected_cities = df[df['platform'].isin(['PS4', 'XOne'])]
print(selected_cities)
```


### Basic Data Manipulation

Pandas makes it easy to modify your DataFrame.

**Adding Columns**:

You can add new columns by simply assigning values to a new column name.

Example:
```python
df['myscore'] = '2'
```


**Modifying Existing Columns**:

To modify a column, apply operations directly.

Example:
```python
df['global_sales'] = df['global_sales'] + 1
```


**Dropping Rows or Columns**:

Use drop() to remove rows or columns.

Example for dropping a column:
```python
df = df.drop('critic_count', axis=1)
```


Example for dropping a row:
```python
df = df.drop(0, axis=0)
```


