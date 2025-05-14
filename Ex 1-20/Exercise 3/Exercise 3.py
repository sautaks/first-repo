"""
Exercise 3:

Select the 'X' column from a DataFrame.
"""
import pandas


def call_dataFrame(data):
    df = pandas.DataFrame(data)
    data_X = df['X']
    print("original Data:")
    print(data)
    print("Select the 'X' column from a DataFrame:")
    print(data_X)


def display_main():
    data = {'X': [1, 2, 3, 4], 'Y': [5, 6, 7, 8]}
    call_dataFrame(data)


if __name__ == '__main__':
    display_main()