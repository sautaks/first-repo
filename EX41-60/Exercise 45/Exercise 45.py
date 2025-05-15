"""
Exercise 45:

Filter rows based on the length of strings in a column.
"""
from pandas import DataFrame


def main():
    data = {'X': ['foo', 'bar', 'baz', 'qux']}
    df = DataFrame(data)
    filter_df = df[df['X'].str.len() > 3]
    print(filter_df)


if __name__ == '__main__':
    main()