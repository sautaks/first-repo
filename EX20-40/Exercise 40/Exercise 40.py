"""
Exercise 40:

Filter rows based on datetime index.
"""
import pandas


def main():
    data_range = pandas.date_range(start='1/1/2024', periods=5, freq='D')
    data = {'X': [1, 2, 3, 4, 5]}
    df = pandas.DataFrame(data, index=data_range)
    filter_df = df['2024-01-02':'2025-01-05']
    print(filter_df)


if __name__ == '__main__':
    main()