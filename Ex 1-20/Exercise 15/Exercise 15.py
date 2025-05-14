"""
Exercise 15:

Merge two DataFrames on a key.
"""
import pandas


def run_dataframe(data1, data2):
    df1 = pandas.DataFrame(data1)
    df2 = pandas.DataFrame(data2)
    merged_df = pandas.merge(df1, df2)
    print(merged_df)


def main():
    data1 = {'key': ['X', 'Y', 'Z'], 'value1': [1, 2, 3]}
    data2 = {'key': ['X', 'Y', 'D'], 'value2': [4, 5, 6]}
    run_dataframe(data1, data2)


if __name__ == '__main__':
    main()