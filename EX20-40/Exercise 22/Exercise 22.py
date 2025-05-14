"""
Exercise 22:

Rename columns in a DataFrame.
"""
import pandas


def run_dataframe(data):
    df = pandas.DataFrame(data)
    df.rename(columns={'X': 'X', 'Y': 'Y'}, inplace=True)
    print(df)


def main():
    data = {'X': [1, 2, 3], 'Y': [4, 5, 6]}
    run_dataframe(data)


if __name__ == '__main__':
    main()