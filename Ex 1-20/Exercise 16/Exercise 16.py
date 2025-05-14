"""
Exercise 16:

Create a pivot table from a DataFrame.
"""
import pandas


def run_dataframe(data):
    df = pandas.DataFrame(data)
    pivottab =  df.pivot_table(values='Z', index='X', columns='Y')
    print(pivottab)


def main():
    data = {'X': ['foo', 'foo', 'bar', 'bar'], 'Y': ['one', 'two', 'one', 'two'], 'Z': [1, 2, 3, 4]}
    run_dataframe(data)


if __name__ == '__main__':
    main()