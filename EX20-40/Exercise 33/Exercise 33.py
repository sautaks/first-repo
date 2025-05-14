"""
Exercise 33:

Change the data type of a column.
"""
import pandas


def main():
    data = {'X': ['1', '2', '3']}
    df = pandas.DataFrame(data)
    df['X'] = df['X'].astype(int)
    print(df)


if __name__ == '__main__':
    main()