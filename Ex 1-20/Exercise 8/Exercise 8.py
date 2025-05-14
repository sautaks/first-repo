"""
Exercise 8:

Group a DataFrame by a column and calculate the mean of each group.
"""
import pandas


class Grouped_data:
    def __init__(self, data):
        self.df = pandas.DataFrame(data)

    def grouping_colmun_data(self):
        group_df = self.df.groupby('X')
        return group_df

    def mean_of_column_data(self):
        mean_df = self.df.groupby('X').mean()
        return mean_df


def display_main():
    data = {'X': [1, 2, 1, 2], 'Y': [5, 6, 7, 8]}
    grouped_data = Grouped_data(data)
    print("Group a DataFrame by a column:")
    print(grouped_data.grouping_colmun_data())
    print("calculate the mean of each group:")
    print(grouped_data.mean_of_column_data())


if __name__ == '__main__':
    display_main()