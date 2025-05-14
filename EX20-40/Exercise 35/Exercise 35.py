"""
Exercise 35:

Create a DataFrame with specified row and column labels.
"""
import pandas


def main():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    df = pandas.DataFrame(data, index=['row1', 'row2', 'row3'],  columns=['col1', 'col2', 'col3'])
    print(df)


if __name__ == '__main__':
    main()