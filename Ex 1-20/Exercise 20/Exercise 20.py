"""
Exercise 20:

Apply a function to each element in a DataFrame.
"""
import pandas


def run_dataframe(data):
    df = pandas.DataFrame(data)
    df= df.apply(lambda col: col.map(lambda x: x * 2))
    print(df)


def main():
    data = {'X': [1, 2, 3], 'Y': [4, 5, 6]}
    run_dataframe(data)


if __name__ == '__main__':
    main()