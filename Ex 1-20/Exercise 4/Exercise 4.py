"""
Exercise 4:

Filter rows based on a column condition.
"""
import pandas


def call_dataFrame(data):
    df = pandas.DataFrame(data)
    filtered_df = df[df['X'] > 2]
    print("original dataframe:")
    print(df)
    print("filtered dataframe:")
    print(filtered_df)



def display_main():
    data = {'X': [1, 2, 3, 4], 'Y': [5, 6, 7, 8]}
    call_dataFrame(data)

if __name__ == '__main__':
    display_main()