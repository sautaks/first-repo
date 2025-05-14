"""
Exercise 24:

Calculate the cumulative sum of a column.
"""
import pandas


def run_pandas(data):
    df = pandas.DataFrame(data)
    df['Cumulative_Sum'] = df['X'].cumsum()
    print(df)



def main():
    data = {'X': [1, 2, 3, 4]}
    run_pandas(data)


if __name__ == '__main__':
    main()