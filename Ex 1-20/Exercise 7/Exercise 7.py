"""
Exercise 7:

Sort a DataFrame by a column.
"""
import pandas


class Sorting_Dataframe:
    def __init__(self,data):
        self.df = pandas.DataFrame(data)

    def sort_by_column(self,col_name,ascending = True):
        self.df = self.df.sort_values(by=col_name,ascending=ascending )

    def get_dataframe(self):
        return self.df


def display_main():
    data = {'X': [4, 3, 2, 1], 'Y': [8, 7, 6, 5]}
    sorting_data = Sorting_Dataframe(data)
    sorting_data.sort_by_column('X')
    df = sorting_data.get_dataframe()
    print("Sorting DataFrame by 'X':")
    print(df)


if __name__ == '__main__':
    display_main()