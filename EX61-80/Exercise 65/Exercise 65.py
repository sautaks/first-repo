"""
Exercise 65:

Create a DataFrame and calculate the z-score of each column.
"""
import numpy
import pandas


def main():
    data = {'X': [1, 2, 3, 4], 'Y': [4, 5, 6, 7]}
    df = pandas.DataFrame(data)
    df['zscore_A'] = (df['X'] - numpy.mean(df['X']))/numpy.std(df['X'])
    df['zscore_B'] = (df['Y'] - numpy.mean(df['Y'])) / numpy.std(df['Y'])
    print(df)

if __name__ == '__main__':
    main()