"""
Exercise 62:

Create a DataFrame with datetime index and resample by month.
"""
import pandas


def main():
    date_range = pandas.date_range(start='1/1/2020', periods=100, freq='D')
    data = {'X': range(100)}
    df = pandas.DataFrame(data, index=date_range)
    monthly_df = df.resample('ME').sum()
    print(monthly_df)


if __name__ == '__main__':
    main()