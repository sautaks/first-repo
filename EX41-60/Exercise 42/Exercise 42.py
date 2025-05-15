"""
Exercise 42:

Create a DataFrame with hierarchical index
"""
import pandas


def main():
    arrays = [['X', 'X', 'Y', 'Y'], [1, 2, 1, 2]]
    index = pandas.MultiIndex.from_arrays(arrays,names=('Group','Number'))
    data = {'Value': [10, 20, 30, 40]}
    df = pandas.DataFrame(data, index= index)
    print(df)


if __name__ == '__main__':
    main()