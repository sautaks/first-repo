"""
Exercise 31:

Create a DataFrame with random values.
"""
import numpy.random
import pandas


def main():
    data = numpy.random.rand(4,3)
    df = pandas.DataFrame(data, columns=['X', 'Y', 'Z'])
    print(df)


if __name__ == '__main__':
    main()