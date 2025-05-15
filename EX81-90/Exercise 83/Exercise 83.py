"""
Exercise 83:

Create a DataFrame and calculate the expanding minimum for each group.
"""
import pandas


def main():
    data = {'X': ['foo', 'bar', 'foo', 'bar'], 'Y': [1, 2, 3, 4]}
    df = pandas.DataFrame(data)
    df['Expanding_Min'] = df.groupby('X')['Y'].expanding().min().reset_index(level=0, drop=True)
    print(df)


if __name__ == '__main__':
    main()