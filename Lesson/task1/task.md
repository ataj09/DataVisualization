# Welcome to Pandas!

Pandas is a powerful library for data manipulation and analysis in Python. 
It provides data structures and functions needed to work with structured data seamlessly. 
One of the first steps in any data analysis workflow is loading your dataset into a DataFrame.

### Key Concepts:

1. **DataFrame**:
   - A DataFrame is a two-dimensional, size-mutable, potentially heterogeneous tabular data structure with labeled axes 
   (rows and columns). It can be thought of as a spreadsheet (Excel) or SQL table. For documentation
    visit [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)

2. **CSV**:
   - Comma-separated values is a text file format that uses commas to separate values, and newlines to separate records.
   

### Why Use Pandas?

- **Ease of Use**: Pandas provides a simple and intuitive interface for data manipulation.
- **Performance**: It is optimized for performance, allowing for fast data processing.
- **Integration**: Works well with other libraries such as NumPy, Matplotlib, and Seaborn for data analysis and visualization.

### Using pandas

Simply have pandas library installed and import it (it is commonly imported as pd)
```python
import pandas as pd
```
### Loading Data:

To load a dataset, you can use the `pd.read_csv(path_to_file)` function. In case you get `FileNotFoundError`
check the path and confirm what file actually exists there, if not, download it [link](https://drive.google.com/drive/folders/18r0XtRXZe_ljb6NfgjUdgnuuINc42SFw)
and place inside `common` directory.

### Inspecting your data

- `df.head(n)` or `df.tail(n)`: Displays first or last `n` rows of Dataframe
- `df.info()`: Provides summary of DataFrame, including data types etc.
- `df.describe()` Generates statistical summary of numeric columns
