"""
Exercise 81:

Create a DataFrame and calculate the cumulative product for each group.
"""
import pandas


def main():
    data = {'X': ['foo', 'bar', 'foo', 'bar'], 'Y': [1, 2, 3, 4]}
    df = pandas.DataFrame(data)
    df['Cumulative_Product'] = df.groupby('X')['Y'].cumprod()
    print(df)


if __name__ == '__main__':
    main()