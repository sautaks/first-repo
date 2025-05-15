"""
Exercise 49:

Calculate the z-score of values in a DataFrame.
"""
import numpy
from pandas import DataFrame


def main():
    data = {'X': [1, 2, 3, 4], 'Y': [4, 5, 6, 7]}
    df = DataFrame(data)
    df['zscore_A'] = (df['X'] - numpy.mean(df['X']))/numpy.std(df['X'])
    print(df)


if __name__ == '__main__':
    main()