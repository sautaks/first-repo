"""
Exercise 87:

Create a DataFrame and calculate the expanding covariance.
"""
import pandas


def main():
    data = {'X': [1, 2, 3, 4], 'Y': [4, 3, 2, 1]}
    df = pandas.DataFrame(data)
    df['Expanding_Cov'] = df['X'].expanding().cov(df['Y'])
    print(df)


if __name__ == '__main__':
    main()