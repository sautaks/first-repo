"""
Exercise 17:

Reshape a DataFrame from long to wide format.
"""
import pandas


def run_dataframe(data):
    df = pandas.DataFrame(data)
    wide_df = df.pivot(index='X', columns='Y', values='Z')
    print(wide_df)


def main():
    data = {'X': ['foo', 'foo', 'bar', 'bar'], 'Y': ['one', 'two', 'one', 'two'], 'Z': [1, 2, 3, 4]}
    run_dataframe(data)


if __name__ == '__main__':
    main()