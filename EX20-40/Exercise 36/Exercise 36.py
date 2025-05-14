"""
Exercise 36:

Transpose a DataFrame.
"""
import pandas


def main():
    data = {'X': [1, 2, 3], 'Y': [4, 5, 6]}
    df = pandas.DataFrame(data)
    transposed_df = df.T
    print(transposed_df)


if __name__ == '__main__':
    main()