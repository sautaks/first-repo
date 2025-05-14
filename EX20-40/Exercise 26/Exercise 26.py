"""
Exercise 26:

Replace values in a DataFrame based on a condition.
"""
import pandas


def main():
    data = {'X': [1, 2, 3, 4], 'Y': [5, 6, 7, 8]}
    df = pandas.DataFrame(data)
    df.loc[df['X'] > 2, 'Y'] = 0
    print(df)


if __name__ == '__main__':
    main()