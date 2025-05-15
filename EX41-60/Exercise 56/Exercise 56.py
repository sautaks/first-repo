"""
Exercise 56:

Create a DataFrame and calculate the rolling standard deviation.
"""
import pandas


def main():
    data = {'X': [1, 2, 3, 4, 5, 6]}
    df = pandas.DataFrame(data)
    df['Rolling_Std'] = df['X'].rolling(window=3).std()
    print(df)


if __name__ == '__main__':
    main()