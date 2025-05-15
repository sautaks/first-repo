"""
Exercise 78:

Create a DataFrame with random values and calculate the z-score for each element.
"""
import numpy.random
import pandas


def main():
    data = numpy.random.rand(4,3)
    df = pandas.DataFrame(data, columns=['X', 'Y', 'Z'])
    df = df.apply(lambda x: (x - x.mean()) / x.std(), axis=0)
    print(df)


if __name__ == '__main__':
    main()