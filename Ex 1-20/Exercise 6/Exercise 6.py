"""
Exercise 6:

Remove a column from a DataFrame.
"""
import pandas


def call_dataFrame(data):
    df = pandas.DataFrame(data)
    df['Z'] = df['X'] % df['Y']
    print("original dataframe: ")
    print(df)
    df.drop(columns=['Z'], inplace=True)
    print("modified dataframe:")
    print(df)


def display_main():
    data = {'X': [1, 2, 3, 4], 'Y': [5, 6, 7, 8]}
    call_dataFrame(data)


if __name__ == '__main__':
    display_main()