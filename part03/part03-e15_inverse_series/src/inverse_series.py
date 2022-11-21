#!/usr/bin/env python3

import pandas as pd

# Gets a Series as a parameter and returns a new series,
# whose indices and values have swapped roles.
def inverse_series(s):
    values = s.values
    indices  = s.index

    inversed_series = pd.Series(indices, index = values)

    return inversed_series

def main():
    series = pd.Series([2, 4, 6, 8], index = list("abcd"))
    print(f"\nORIGINAL:\n{series}")

    inversed_series = inverse_series(series)
    print(f"\nINVERSED:\n{inversed_series}")

if __name__ == "__main__":
    main()
