"""
Exercise 47:

Create a DataFrame from a dictionary of Series.
"""
from pandas import Series, DataFrame


def main():
    data = {'X': Series([1,2,3]), 'Y': Series([4,5,6])}
    df = DataFrame(data)
    print(df)


if __name__ == '__main__':
    main()