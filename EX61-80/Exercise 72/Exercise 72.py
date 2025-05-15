"""
Exercise 72:

Create a DataFrame and calculate the interquartile range (IQR
"""
import numpy.random
import pandas


def main():
    data = numpy.random.rand(4,3)
    df = pandas.DataFrame(data, columns=['X', 'Y', 'Z'])
    Q1 = df.quantile(.25)
    Q3 = df.quantile(.75)
    IQR = Q3-Q1
    print(IQR)


if __name__ == '__main__':
    main()