"""
Exercise 100:

Create a DataFrame and calculate the expanding sum for each group.
"""
import pandas


def main():
    data = {'X': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'bar'], 'Y': range(10)}
    df = pandas.DataFrame(data)
    df['Expanding_Sum'] = df.groupby('X')['Y'].expanding().sum().reset_index(level=0, drop=True)
    print(df)


if __name__ == '__main__':
    main()