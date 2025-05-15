"""
Exercise 43:

Calculate the difference between consecutive rows in a DataFrame.
"""
import pandas


def main():
    data = {'X': [1, 3, 6, 10]}
    df = pandas.DataFrame(data)
    df['Difference'] = df['X'].diff()
    print(df)


if __name__ == '__main__':
    main()