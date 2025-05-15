"""
Exercise 73:

Create a DataFrame with datetime index and calculate the rolling mean.
"""
import pandas


def main():
    date_range = pandas.date_range(start='1/1/2025', periods=10, freq='D')
    data = {'X': range(10)}
    df = pandas.DataFrame(data, index=date_range)
    df['Rolling_Mean'] = df['X'].rolling(window=3).mean()
    print(df)


if __name__ == '__main__':
    main()