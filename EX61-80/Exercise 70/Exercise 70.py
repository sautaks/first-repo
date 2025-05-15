"""
Exercise 70:

Create a DataFrame and apply a custom function to each row.
"""
import pandas


def main():
    data = {'X': [1, 2, 3], 'Y': [4, 5, 6]}
    df = pandas.DataFrame(data)
    df['Sum'] = df.apply(lambda row: row['X'] + row['Y'], axis=1)
    print(df)


if __name__ == '__main__':
    main()