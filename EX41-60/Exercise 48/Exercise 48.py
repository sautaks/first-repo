"""
Exercise 48:

Filter rows based on whether a column value is in a list.
"""
from pandas import DataFrame


def main():
    data = {'X': [1, 2, 3, 4], 'Y': [5, 6, 7, 8]}
    df = DataFrame(data)
    filter_df = df[df['X'].isin([2,3])]
    print(filter_df)


if __name__ == '__main__':
    main()