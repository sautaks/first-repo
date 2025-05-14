import pandas


def detect_row_dataFrame(data):
    framedata = pandas.DataFrame(data)
    first_3_rows = framedata.head(3)
    print("original data:")
    print(data)
    print("First 3 rows:")
    print(first_3_rows)
def display_main():
    data = {'X': [1, 2, 3, 4], 'Y': [5, 6, 7, 8]}
    detect_row_dataFrame(data)


if __name__ == '__main__':
    display_main()