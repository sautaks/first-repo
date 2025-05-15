"""
Exercise 82:

Create a DataFrame with random values and calculate the expanding sum.
"""
import numpy.random
import pandas


def main():
    data = numpy.random.rand(4,3)
    df = pandas.DataFrame(data, columns=['X','Y','Z'])
    df['Expanding_Sum'] = df['X'].expanding().sum()
    print(df)


if __name__ == '__main__':
    main()