"""
Exercise 9:

Replace missing values in a DataFrame.
"""
import pandas


class Replacing_Missing_values:
    def __init__(self,data):
        self.df = pandas.DataFrame(data)

    def replacing_missing_data(self):
        self.df.fillna(0, inplace=True)
        return self.df



def main():
    data = {'X': [1, 2, None, 4], 'Y': [5, None, 7, 8]}
    replacing_data = Replacing_Missing_values(data)
    print("Replace missing values in a DataFrame")
    print(replacing_data.replacing_missing_data())


if __name__ == '__main__':
    main()