"""
Exercise 23:

Filter rows by multiple conditions.
"""
import pandas


def run_dataframe(data):
    df = pandas.DataFrame(data)
    filter_df = df[(df['X'] > 2) & (df['Y'] < 7)]
    print(filter_df)


def main():
    data = {'X': [1, 2, 3, 4], 'Y': [4, 5, 6, 7]}
    run_dataframe(data)


if __name__ == '__main__':
    main()