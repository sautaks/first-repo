"""
Exercise 60:

Create a DataFrame and calculate the rolling correlation between two columns.
"""
import pandas


def main():
    data = {'X': [1, 2, 3, 4, 5, 6], 'Y': [6, 5, 4, 3, 2, 1]}
    df = pandas.DataFrame(data)
    df['Rolling_Corr'] = df['X'].rolling(window=3).corr(df['Y'])
    print(df)


if __name__ == '__main__':
    main()