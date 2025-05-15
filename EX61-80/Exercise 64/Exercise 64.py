"""
Exercise 64:

Create a DataFrame with random integers and calculate the mode.
"""
import numpy.random
import pandas


def main():
    data = numpy.random.randint(1, 10, size=(5,3))
    df = pandas.DataFrame(data, columns=['X', 'Y', 'Z'])
    print(df.mode())


if __name__ == '__main__':
    main()