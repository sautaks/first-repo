"""
Exercise 59:

Create a DataFrame with random values and calculate the correlation matrix.
"""
import numpy
import pandas


def main():
    data = numpy.random.rand(4, 3)
    df = pandas.DataFrame(data, columns=['X', 'Y', 'Z'])
    print(df.corr())

if __name__ == '__main__':
    main()