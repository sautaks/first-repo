"""
Exercise 21:

Create a DataFrame from a list of dictionaries.
"""
import pandas


def run_dataframe(data):
    df = pandas.DataFrame(data)
    print(df)


def main():
    data = [{'X': 1, 'Y': 2}, {'X': 3, 'Y': 4}]
    run_dataframe(data)


if __name__ == '__main__':
    main()