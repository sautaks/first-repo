"""
Exercise 41:

Create a DataFrame with duplicate rows and remove duplicates.
"""
import pandas


def main():
    data = {'X': [1, 2, 2, 3], 'Y': [4, 5, 5, 6]}
    df = pandas.DataFrame(data)
    df.drop_duplicates(inplace=True)
    print(df)


if __name__ == '__main__':
    main()