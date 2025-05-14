"""
Exercise 12:

Calculate the sum of values in each column.
"""
import pandas


def run_dataframe(data):
    dframe = pandas.DataFrame(data)
    print(dframe.sum())


def main():
    data = {'X': [1,2,3], 'Y':[4,5,6]}
    run_dataframe(data)


if __name__ == '__main__':
    main()