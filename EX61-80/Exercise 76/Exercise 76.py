"""
Exercise 76:

Create a DataFrame with random values and calculate the cumulative variance.
"""
import numpy.random
import pandas


def main():
    data = numpy.random.rand(10, 3)
    df = pandas.DataFrame(data, columns=['X', 'Y', 'Z'])
    df['Cumulative_Var'] = df['X'].expanding().var()
    print(df)

if __name__ == '__main__':
    main()