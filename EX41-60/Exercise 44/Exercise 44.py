"""
Exercise 44:

Create a DataFrame with hierarchical columns.
"""
from pandas import MultiIndex, DataFrame


def main():
    arrays = [['X', 'X', 'Y', 'Y'], ['C1', 'C2', 'C1', 'C2']]
    columns = MultiIndex.from_arrays(arrays, names=('Group', 'Type'))
    data = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    df = DataFrame(data, columns=columns)
    print(df)


if __name__ == '__main__':
    main()