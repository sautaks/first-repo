"""
Exercise 93:

Create a DataFrame with random values and calculate the rolling standard deviation for each group.
"""
import numpy.random
import pandas


def main():
    data = numpy.random.rand(10,3)
    df = pandas.DataFrame(data, columns=['X', 'Y', 'Z'])
    df['Rolling_std_dev'] = df.groupby('X')['Y'].rolling(window= 3).std().reset_index(level= 0, drop= True)
    print(df)

if __name__ == '__main__':
    main()