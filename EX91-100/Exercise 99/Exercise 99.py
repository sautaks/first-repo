"""
Exercise 99:

Create a DataFrame with random values and calculate the rolling median for each group.
"""
import numpy.random
import pandas


def main():
    data = numpy.random.rand(10,3)
    df = pandas.DataFrame(data, columns=['X', 'Y', 'Z'])
    df['Rolling_Median'] = df.groupby('X')['Y'].rolling(window = 3).median().reset_index(level=0, drop=True)
    print(df)

if __name__ == '__main__':
    main()