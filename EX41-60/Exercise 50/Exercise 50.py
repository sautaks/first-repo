"""
Exercise 50:

Create a DataFrame with random integers and calculate descriptive statistics.
"""
import numpy
from pandas import DataFrame


def main():
    data = numpy.random.randint(1, 100, size=(5,3))
    df = DataFrame(data, columns=['X', 'Y', 'Z'])
    print(df.describe())


if __name__ == '__main__':
    main()