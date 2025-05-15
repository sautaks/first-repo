"""
Exercise 67:

Create a DataFrame and apply a custom function to each column.
"""
import pandas


def main():
    data = {'X' : [1,2,3], 'Y':[4,5,6]}
    df = pandas.DataFrame(data)
    df = df.apply(lambda x:x+1)
    print(df)


if __name__ == '__main__':
    main()