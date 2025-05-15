"""
Exercise 63:

Create a DataFrame and calculate the exponential moving average.
"""
import pandas


def main():
    data = {'X': [1,2,3,4,5,6]}
    df = pandas.DataFrame(data)
    df['EMA'] = df['X'].ewm(span=3, adjust=False).mean()
    print(df)


if __name__ == '__main__':
    main()