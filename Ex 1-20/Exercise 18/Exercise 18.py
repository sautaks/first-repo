"""
Exercise 18:

Calculate the correlation between columns in a DataFrame
"""
from statistics import correlation

import pandas


def run_dataframe(data):
    df = pandas.DataFrame(data)
    correlation = df.corr()
    print(correlation)


def main():
    data = {'X': [1, 2, 3, 4], 'Y': [4, 3, 2, 1]}
    run_dataframe(data)


if __name__ == '__main__':
    main()