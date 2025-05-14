"""
Exercise 19:

Iterate over rows in a DataFrame using iterrows().
"""
import pandas


def run_dataframe(data):
    df = pandas.DataFrame(data)
    for index, row in df.iterrows():
        print(index, row['X'], row['Y'])


def main():
    data = {'X': [1, 2, 3], 'Y': [4, 5, 6]}
    run_dataframe(data)


if __name__ == '__main__':
    main()