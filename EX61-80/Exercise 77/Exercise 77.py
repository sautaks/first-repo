"""
Exercise 77:

Create a DataFrame and apply a custom function to each element.
"""
import pandas

#Define the custom function
def custom_function(x):
    return x * 2

def main():# Create a DataFrame
    data = {'X' : [1,2,3], 'Y' : [4,5,6]}
    df = pandas.DataFrame(data)
    df = df.apply(lambda col: col.map(custom_function))
    print(df)


if __name__ == '__main__':
    main()