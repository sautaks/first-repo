"""
Exercise 89:

Create a DataFrame and calculate the expanding median.
"""
import pandas


def main():
    data = {'X' : [1,2,3,4,5,6]}
    df = pandas.DataFrame(data)
    df['Expanding_Median'] = df['X'].expanding().median()
    print(df)


if __name__ == '__main__':
    main()