import pandas as pd
import numpy as np


def clean_cols(df):

    cols = df.columns

    # Remove special characters
    cols = cols.map(
        lambda x: x.replace(' ', '_').replace('(', '_').
        replace(')', '').replace('/', '').replace('%', '_').
        replace('-', '').replace('*', '_').replace('__', '_')
        if isinstance(x, (str, unicode)) else x)

    # Special case: remove special characters from the start and end of
    # column names
    for col in cols:
        if col.endswith('_'):
            cols[cols == col] = col[:-1]
        if col.startswith('_'):
            cols[cols == col] = col[1:]

    # Set column names to cleaned version
    df.columns = cols

# Test script
df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=[
    '_ab', 'B', 'asd*q*', 'd)*/a)'])
print list(df.columns.values)
clean_cols(df)
print list(df.columns.values)
