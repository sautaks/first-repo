"""
Exercise 61:

Create a DataFrame and calculate the expanding variance.
"""
import pandas


def main():
    data = {'X': [1, 2, 3, 4, 5, 6]}
    df = pandas.DataFrame(data)
    df['Expanding_Var'] = df['X'].expanding().var()
    print(df)


if __name__ == '__main__':
    main()