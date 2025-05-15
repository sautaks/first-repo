"""
Exercise 74:

Create a DataFrame and calculate the cumulative maximum.
"""
import pandas


def main():
    data = {'X': [1,2,3,2,1]}
    df = pandas.DataFrame(data)
    df['Cumulative_Max'] = df['X'].cummax()
    print(df)


if __name__ == '__main__':
    main()