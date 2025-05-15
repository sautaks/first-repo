"""
Exercise 86:

Create a DataFrame with random values and calculate the expanding standard deviation.
"""
import numpy.random
import pandas


def main():
    data = numpy.random.rand(4,3)
    df = pandas.DataFrame(data, columns=['X', 'Y', 'Z'])
    df['Expanding_Std'] = df['X'].expanding().std()
    print(df)


if __name__ == '__main__':
    main()