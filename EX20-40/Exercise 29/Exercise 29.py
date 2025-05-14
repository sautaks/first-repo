"""
Exercise 29:

Create a DataFrame from a list of tuples.
"""
import pandas

def main():
    data = [(1, 2), (3, 4), (5, 6)]
    df = pandas.DataFrame(data, columns=['X','Y'])
    print(df)


if __name__ == '__main__':
    main()