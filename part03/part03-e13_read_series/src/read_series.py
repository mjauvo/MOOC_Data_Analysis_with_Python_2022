#!/usr/bin/env python3

import pandas as pd

# Reads input lines from the user and return a Series. Each
# line contains first the index and then the corresponding value,
# separated by whitespace. The index and values are strings (in
# this case dtype is object). An empty line signals the end of
# Series. Malformed input should cause an exception. An input line
# is malformed, if it is non-empty and, when split at whitespace,
# does not result in two parts.
def read_series():
    indices = []
    values  = []

    while True:
        user_input = input("Type index and value separated by whitespace: ")

        if user_input == "":
            break
        else:
            try:
                index, value = user_input.split()
                indices.append(index)
                values.append(value)
            except ValueError:
                print("Malformed input was given!!")
                continue

    result = pd.Series(data=values, index=indices, dtype=object)

    return result

def main():
    series = read_series()
    print(series)

if __name__ == "__main__":
    main()
