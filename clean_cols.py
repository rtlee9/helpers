def clean_cols(df):
    cols = df.columns
    cols = cols.map(lambda x: x.replace(' ', '_').replace('(', '_').
                    replace(')', '').replace('/', '').replace('%', '_').
                    replace('-', '').replace('__', '_')
                    if isinstance(x, (str, unicode)) else x)
    df.columns = cols
