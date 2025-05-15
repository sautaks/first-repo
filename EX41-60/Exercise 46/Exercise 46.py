"""
Exercise 46:

Calculate the percentage change between rows in a DataFrame.
"""
from pandas import DataFrame


def main():
    data = {'X': [1, 2, 3, 4]}
    df = DataFrame(data)
    df['Pct_Change'] = df['X'].pct_change()
    print(df)


if __name__ == '__main__':
    main()