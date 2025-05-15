"""
Exercise 53:

Create a DataFrame with random values and calculate the skewness.
"""
import pandas as pd
import numpy as np


if __name__ == '__main__':

    # 1. Define DataFrame dimensions
    num_rows = 100
    num_cols = 5
    column_names = [f'Col_{i + 1}' for i in range(num_cols)]  # e.g., ['Col_1', 'Col_2', ..., 'Col_5']

    # 2. Generate random data
    # We'll use np.random.randn which generates samples from the standard normal distribution (mean=0, std=1)
    # You could also use np.random.rand for uniform distribution [0,1) or other distributions.
    random_data = np.random.randn(num_rows, num_cols)

    # 3. Create the Pandas DataFrame
    df = pd.DataFrame(random_data, columns=column_names)

    # Display the first few rows of the DataFrame
    print("--- Generated DataFrame (First 5 rows) ---")
    print(df.head())
    print("\n" + "=" * 40 + "\n")  # Separator

    # 4. Calculate Skewness
    # The .skew() method calculates the sample skewness for each column (axis=0 by default).
    # Skewness is a measure of the asymmetry of the probability distribution of a real-valued random variable about its mean.
    # - Skewness = 0: Normal distribution (symmetric).
    # - Skewness > 0: More weight in the right tail of the distribution (right-skewed).
    # - Skewness < 0: More weight in the left tail of the distribution (left-skewed).
    skewness_values = df.skew()

    # Display the calculated skewness
    print("--- Skewness of each column ---")
    print(skewness_values)

    print("\n--- Interpretation Notes ---")
    print(" - Values close to 0 suggest relatively symmetric data distribution for that column.")
    print(" - Positive values indicate a right-skewed distribution (tail is longer on the right).")
    print(" - Negative values indicate a left-skewed distribution (tail is longer on the left).")
    print(" - Since we used np.random.randn (standard normal), we expect skewness values near 0,")
    print("   but they won't be exactly 0 due to random sampling variation.")