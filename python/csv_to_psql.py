import argparse
import pandas as pd
import numpy as np


def cols_by_type(df, dtype):
    """ Return all column names in `df` with data type `dtype`
    """
    return [col for col, dtype in zip(df.columns, df.dtypes) if dtype == dtype]


def parse_col_name(col_name):
    """ Standardize column name `col_name`
    """
    return col_name.upper().strip()


def append_not_null(col, sql_str):
    """ Append 'NOT NULL' to `sql_str` if no nulls are present in column `col`
    """
    not_null = ' NOT NULL' if col.isnull().sum() == 0 else ''
    return '{}{}'.format(sql_str, not_null)


def parse_obect_col(df, col_name):
    """ Return column create string for string columns
    """
    col = df[col_name]
    max_len = col.str.len().max()
    return append_not_null(col, '{} VARCHAR({:.0f})'.format(parse_col_name(col_name), max_len))


def parse_int_col(df, col_name):
    """ Return column create string for int columns
    """
    col = df[col_name]
    max_int = col.max()
    min_int = col.min()

    if max_int < 32767 and min_int > -32768:
        int_type = 'SMALLINT'
    elif max_int < 2147483647 and min_int > -2147483648:
        int_type = 'INT'
    elif max_int < 9223372036854775807 and min_int > -9223372036854775808:
        int_type = 'BIGINT'
    else:
        int_type = 'BIGINT'

    return append_not_null(col, '{} {}'.format(parse_col_name(col_name), int_type))


def parse_float_col(df, col_name):
    """ Return column create string for float columns
    """
    col = df[col_name]
    float_type = 'REAL'
    return append_not_null(col, '{} {}'.format(parse_col_name(col_name), float_type))


def main(filename):
    """ Create PSQL insert statement for data table specified by `filename`
    """
    df = pd.read_csv(filename, low_memory=False)

    parse_fn_lookup = {
        np.dtype('O'): parse_obect_col,
        np.dtype('int64'): parse_int_col,
        np.dtype('float64'): parse_float_col,
    }

    for col, dtype in zip(df.columns, df.dtypes):
        print(parse_fn_lookup[dtype](df, col) + ',')


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--filename', type=str, required=True, help='path to dataset')
    args = p.parse_args()
    main(args.filename)
