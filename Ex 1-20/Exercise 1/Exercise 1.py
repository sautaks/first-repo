"""
Exercise 1:

Create a DataFrame from a dictionary of lists.
"""
import pandas


def call_dataFrame(data):
    data_frame = pandas.DataFrame(data)
    print("Dictionary data:")
    print(data)
    print("DataFrame created from Dictionary of lists:")
    print(data_frame)


def display_main():
    data = {'X': [1, 2, 3, 4], 'Y': [5, 6, 7, 8]}
    call_dataFrame(data)


if __name__ == '__main__':
    display_main()