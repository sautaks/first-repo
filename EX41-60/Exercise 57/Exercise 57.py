"""
Exercise 57:

Create a DataFrame and calculate the expanding mean.
"""
import pandas


def main():
    data = {'X': [1, 2, 3, 4, 5, 6]}
    df = pandas.DataFrame(data)
    df['Expanding_Mean'] = df['X'].expanding().mean()
    print(df)


if __name__ == '__main__':
    main()