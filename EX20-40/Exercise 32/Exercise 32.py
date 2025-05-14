"""
Exercise 32:

Calculate the rank of values in a DataFrame.
"""
import pandas


def main():
    data = {'X': [3, 1, 4, 1], 'Y': [2, 3, 1, 4]}
    df = pandas.DataFrame(data)
    df['Rank'] = df['X'].rank()
    print(df)


if __name__ == '__main__':
    main()