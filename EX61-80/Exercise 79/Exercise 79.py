"""
Exercise 79:

Create a DataFrame and calculate the cumulative sum for each group.
"""
import pandas


def main():
    data = {'X': ['foo', 'bar', 'foo', 'bar'], 'Y': [1, 2, 3, 4]}
    df = pandas.DataFrame(data)
    df['Cumulayive_Sum'] = df.groupby('X')['Y'].cumsum()
    print(df)


if __name__ == '__main__':
    main()