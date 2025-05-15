"""
Exercise 55:

Calculate the cumulative product of a column in a DataFrame.
"""
import pandas


def main():
    data = {'X': [1,2,3,4] }
    df = pandas.DataFrame(data)
    df['Cumulative_ Product'] = df['X'].cumprod()
    print(df)


if __name__ == '__main__':
    main()