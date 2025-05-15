"""
Exercise 52:

Filter rows based on multiple string conditions.
"""
from pandas import DataFrame


def main():
    data = {'X': ['foo', 'bar', 'baz', 'qux']}
    df = DataFrame(data)
    filter_df = df[df['X'].str.contains('ba|qu')]
    print(filter_df)


if __name__ == '__main__':
    main()