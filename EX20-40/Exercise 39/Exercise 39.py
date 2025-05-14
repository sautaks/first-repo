"""
Exercise 39:

Add a prefix or suffix to column names.
"""
import pandas


def main():
    data = {'X': [1, 2, 3], 'Y': [4, 5, 6]}
    df = pandas.DataFrame(data)
    df = df.add_prefix('col_')
    print(df)



if __name__ == '__main__':
    main()