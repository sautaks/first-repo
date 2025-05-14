"""
Exercise 37:

Set a column as the index of a DataFrame.
"""
import pandas


def main():
    data = {'X': [1, 2, 3], 'Y': [4, 5, 6]}
    df = pandas.DataFrame(data)
    df.set_index('X', inplace=True)
    print(df)


if __name__ == '__main__':
    main()