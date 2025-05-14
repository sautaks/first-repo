"""
Exercise 34:

Filter rows based on string matching.
"""
import pandas


def main():
    data = {'X': ['foo', 'bar', 'baz', 'qux']}
    df = pandas.DataFrame(data)
    filter_df = df[df['X'].str.contains('ba')]
    print(filter_df)


if __name__ == '__main__':
    main()