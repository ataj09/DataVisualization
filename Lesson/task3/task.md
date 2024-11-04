# Plotting Data with Seaborn

In the previous chapters, we explored how to manipulate and retrieve data from DataFrames using Pandas. Data visualization is an essential part of data analysis, as it helps in understanding trends, patterns, and insights that might not be immediately apparent from the raw data. In this chapter, we will learn how to create various types of plots using Seaborn, a powerful visualization library built on top of Matplotlib that provides a high-level interface for drawing attractive statistical graphics.

In this task, you will use matplotlib and seaborn as primary visualization libraries.
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```

### Basic Plotting with Seaborn

Seaborn provides a variety of plotting functions that can be used directly with Pandas DataFrames.

### Line Plot

Line plots are used to visualize data points over a continuous interval. Here’s how to create a simple line plot using Seaborn:

```python
sns.lineplot(data=df, x='year', y='global_sales')
plt.title('Global Sales Over Years')
plt.xlabel('Year')
plt.ylabel('Global Sales (in millions)')
plt.show()
```

### Bar Plot

Bar plots are useful for comparing quantities associated with different groups. Here’s how to create a bar plot:

```python
sns.barplot(x='platform', y='global_sales', data=df, estimator=sum, ci=None)
plt.title('Total Global Sales by Platform')
plt.xlabel('Platform')
plt.ylabel('Total Global Sales (in millions)')
plt.xticks(rotation=45)
plt.show()
```

### Histogram

Histograms are great for visualizing the distribution of a dataset. You can create a histogram of the 'global_sales' column like this:

```python
sns.histplot(df['global_sales'], bins=30, kde=True)
plt.title('Distribution of Global Sales')
plt.xlabel('Global Sales (in millions)')
plt.show()
```

### Scatter Plot

Scatter plots are useful for observing the relationship between two numeric variables. Here’s how to create a scatter plot:

```python
sns.scatterplot(x='critic_score', y='global_sales', data=df)
plt.title('Global Sales vs. Critic Score')
plt.xlabel('Critic Score')
plt.ylabel('Global Sales (in millions)')
plt.show()
```

### Customizing Plots

Seaborn allows for extensive customization of plots:

- **Color Palettes**: You can change the color palette using `sns.set_palette()`.
- **Themes**: Seaborn comes with several built-in themes that can be applied using `sns.set_style()`.

Example of a customized plot:

```python
sns.set_theme(style="whitegrid")
sns.barplot(x='platform', y='global_sales', data=df, estimator=sum, ci=None, palette='Blues')
plt.title('Total Global Sales by Platform')
plt.xlabel('Platform')
plt.ylabel('Total Global Sales (in millions)')
plt.xticks(rotation=45)
plt.show()
```
