"""
Exercise 11:

Create a DataFrame with specific column names.
"""
import pandas


class New_DataFrame:
    def __init__(self,data):
        self.df = pandas.DataFrame(data)

    def get_dataframe(self):
        return self.df

def main():
    data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
    new_col_data = New_DataFrame(data)
    print("Create a DataFrame with specific column names:")
    print(new_col_data.get_dataframe())


if __name__ == '__main__':
    main()