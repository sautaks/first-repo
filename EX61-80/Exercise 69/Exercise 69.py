"""
Exercise 69:

Create a DataFrame and calculate the percentage of missing values in each column.
"""
import pandas


def main():
    data = {'X': [1, 2, None, 4], 'Y': [4, None, 6, 8]}
    df = pandas.DataFrame(data)
    missing_percentage = df.isnull().mean() * 100
    print(missing_percentage)


if __name__ == '__main__':
    main()