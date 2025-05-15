"""
Exercise 84:

Create a DataFrame with random values and calculate the expanding maximum for each group.
"""
import numpy.random
import pandas


def main():
    data = numpy.random.rand(4,3)
    df = pandas.DataFrame(data, columns=['X', 'Y', 'Z'])
    df['Expanding_Min'] = df.groupby('X')['Y'].expanding().max().reset_index(level= 0, drop=True)
    print(df)


if __name__ == '__main__':
    main()