"""
Exercise 28:

Calculate the rolling mean of a column.
"""
import pandas


def run_dataframe(data):
    df = pandas.DataFrame(data)
    df['Rolling_Mean'] = df['X'].rolling(window=3).mean()
    print(df)


def main():
    data = {'X': [1, 2, 3, 4, 5, 6]}
    run_dataframe(data)


if __name__ == '__main__':
    main()