"""
Exercise 27:

Create a DataFrame with a MultiIndex.
"""
from operator import index

import pandas


def run_dataframe(arrays, data):
    index = pandas.MultiIndex.from_arrays(arrays, names=('Group', 'Number'))
    df = pandas.DataFrame(data,index=index)
    print(df)


def main():
    arrays = [['X', 'X', 'Y', 'Y'], [1, 2, 1, 2]]
    data = {'Value': [10, 20, 30, 40]}
    run_dataframe(arrays,data)


if __name__ == '__main__':
    main()