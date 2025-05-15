"""
Exercise 54:

Create a DataFrame and calculate the kurtosis.
"""
import numpy.random
import pandas


def main():
    data = numpy.random.rand(4,3)
    df = pandas.DataFrame(data, columns=['X', 'Y', 'Z'])
    print(df.kurt())


if __name__ == '__main__':
    main()