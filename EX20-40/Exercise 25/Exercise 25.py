"""
Exercise 25:

Drop rows with missing values.
"""
import pandas


def run_dataframe(data):
    df = pandas.DataFrame(data)
    df.dropna(inplace=True)
    print(df)


def main():
    data = {'X': [1, 2, None, 4], 'Y': [4, 5, 6, None]}
    run_dataframe(data)


if __name__ == '__main__':
    main()