"""
Exercise 95:

Create a DataFrame with random values and calculate the rolling correlation for each group.
"""
import numpy.random
import pandas


def main():
    numpy.random.seed(42)
    data = numpy.random.rand(10,3)
    df = pandas.DataFrame(data, columns=['X', 'Y', 'Z'])
    df['Group'] = numpy.random.choice(['A', 'B'], size=10)
    df['Rolling_Corr'] = df.groupby('Group').apply(lambda group: group['Y'].rolling(window=3).corr(group['Z'])).reset_index(level= 0, drop=True)
    print(df)

if __name__ == '__main__':
    main()