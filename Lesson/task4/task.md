# Final Task
As for your final task, you should visualize number of games
per genre grouped by platforms. It should look like following


![Error](../../common/example.png)


### How to obtain results
1. **Prepare a dataframe with only neccessery data**
2. **Plot it :D**

### Tips

For grouping, you can use dataframes `groupby()`, `size()` and `reset_index()`.

example
```python
    platform_genre_counts = df.groupby(['col1', 'col2']).size().reset_index(name='count')
```