"""
Exercise 90:

Create a DataFrame with datetime index and calculate the expanding mean for each group.
"""
import pandas


def main():
    data_range = pandas.date_range(start='1/1/2025', periods=10, freq='D')
    data = {'X': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'bar'], 'Y': range(10)}
    df = pandas.DataFrame(data, index=data_range)
    df['Expanding_Mean'] = df.groupby('X')['Y'].expanding().mean().reset_index(level = 0, drop=True)
    print(df)


if __name__ == '__main__':
    main()