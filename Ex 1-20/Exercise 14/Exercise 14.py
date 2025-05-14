"""
Exercise 14:

Concatenate two DataFrames.
"""
import pandas


def run_dataframe(data1, data2):
    df1 = pandas.DataFrame(data1)
    df2 = pandas.DataFrame(data2)
    result = pandas.concat([df1,df2],axis=1)
    print(result)


def main():
    data1 = {'X': [1, 2, 3]}
    data2 = {'Y': [4, 5, 6]}
    run_dataframe(data1,data2)


if __name__ == '__main__':
    main()