"""
Exercise 88:

Create a DataFrame with random values and calculate the expanding correlation.
"""
import numpy.random
import pandas


def main():
    data = numpy.random.rand(4,3)
    df = pandas.DataFrame(data, columns=['X', 'Y', 'Z'])
    df['Expanding_corr'] = df['X'].expanding().corr(df['Y'])
    print(df)

if __name__ == '__main__':
    main()
