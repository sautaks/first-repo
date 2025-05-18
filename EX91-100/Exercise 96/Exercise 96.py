"""
Exercise 96:

Create a DataFrame and calculate the rolling covariance for each group.
"""
import pandas


def main():
    data = {'X': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'bar'],'Y': range(10), 'Z': range(10, 20)}
    df = pandas.DataFrame(data)
    rolling_cov = df.groupby('X').apply(lambda group: group['Y'].rolling(window=3).cov(group['Z'])).reset_index(level = 0, drop=True)
    df['Rolling_Cov'] = rolling_cov
    print(df)


if __name__ == '__main__':
    main()