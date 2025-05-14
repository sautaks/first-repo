"""
Exercise 5:

Add a new column to an existing DataFrame.
"""
import pandas


def call_dataFrame(data):
    df = pandas.DataFrame(data)
    print("original dataframe:")
    print(df)
    df['Z'] = df['X'] + df['Y']
    print("Add column in original dataframe:")
    print(df)


def display_main():
    data = {'X': [1, 2, 3, 4], 'Y': [5, 6, 7, 8]}
    call_dataFrame(data)


if __name__ == '__main__':
    display_main()