"""
Exercise 80:

Create a DataFrame with random values and calculate the rank for each element.
"""
import numpy.random
import pandas


def main():
    data = numpy.random.rand(4,3)
    df = pandas.DataFrame(data, columns=['X', 'Y', 'Z'])
    df = df.rank()
    print(df)


if __name__ == '__main__':
    main()