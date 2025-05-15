"""
Exercise 68:

Create a DataFrame with hierarchical index and calculate the mean for each group.
"""
import pandas


def main():
    arrays = [['X','X','Y','Y'], [1,2,1,2]]
    index = pandas.MultiIndex.from_arrays(arrays, names=('Group', 'Number'))
    data = {'Value': [10,20,30,40]}
    df = pandas.DataFrame(data, index= index)
    group_df = df.groupby('Group').mean()
    print(group_df)


if __name__ == '__main__':
    main()