"""
Exercise 30:

Add a row to a DataFrame.
"""
import pandas


def run_frame(data):
    df = pandas.DataFrame(data)
    new_row = pandas.DataFrame({'X': [5], 'Y': [6]})
    df = pandas.concat([df, new_row], ignore_index=True)
    print(df)


def main():
    data = {'X': [1, 2], 'Y': [3, 4]}
    run_frame(data)


if __name__ == '__main__':
    main()