"""
Exercise 10:

Convert a column to datetime.
"""
import pandas


class Convert_colmun_datatime:
    def __init__(self,data):
        self.df = pandas.DataFrame(data)

    def convert_colmun_to_datatime(self):
        self.df['X']= pandas.to_datetime(self.df['X'])
        return self.df


def display_main():
    data = {'X': ['2020-01-01', '2020-01-02', '2020-01-03']}
    datetime_creation_data = Convert_colmun_datatime(data)
    print("Convert a column to datetime.")
    res_def = datetime_creation_data.convert_colmun_to_datatime()
    print(res_def)


if __name__ == '__main__':
    display_main()