"""
Exercise 75:

Create a DataFrame and calculate the cumulative minimum.
"""
import pandas


def main():
    data = {'X' : [1,2,3,2,1]}
    df = pandas.DataFrame(data)
    df['Cumulative_matrix'] = df['X'].cummin()
    print(df)


if __name__ == '__main__':
    main()