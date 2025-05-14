"""
Exercise 13:

Calculate the mean of values in each row
"""
import pandas


def run_dataframe(data):
    df=pandas.DataFrame(data)
    mean = df.mean()
    print(mean)


def main():
    data = {'X': [1,2,3], 'Y':[4,5,6]}
    run_dataframe(data)


if __name__ == '__main__':
    main()