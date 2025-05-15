"""
Exercise 51:

Calculate the rank of values in each column of a DataFrame.
"""
from pandas import DataFrame


def main():
    data = {'X': [3, 1, 4, 1], 'Y': [2, 3, 1, 4]}
    df = DataFrame(data)
    df['Rank_A'] = df['X'].rank()
    df['Rank_B'] = df['Y'].rank()
    print(df)


if __name__ == '__main__':
    main()