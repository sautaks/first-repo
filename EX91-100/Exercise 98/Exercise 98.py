"""
Exercise 98:

Create a DataFrame and calculate the rolling kurtosis for each group.
"""
import pandas


def main():
    data = {'X': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'bar'], 'Y': range(10)}
    df = pandas.DataFrame(data)
    df['Rolling_Kurt'] = df.groupby('X')['Y'].rolling(window=3).kurt().reset_index(level=0, drop=True)
    print(df)


if __name__ == '__main__':
    main()