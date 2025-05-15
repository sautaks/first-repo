"""
Exercise 71:

Create a DataFrame with random values and calculate the quantiles.
"""
import numpy.random
import pandas


def main():
    data = numpy.random.rand(4,3)
    df = pandas.DataFrame(data, columns=('X','Y','Z'))
    print(df.quantile([0.25, 0.5, 0.75]))

if __name__ == '__main__':
    main()