#!/usr/bin/env python3

import pandas as pd

# Gets two lists of numbers (L1, L2) of length 3 as parameters and
# creates two Series, s1 and s2. The first series has values from
# the first parameter list L1 and has corresponding indices a, b,
# and c. The second series gets its values from the second parameter
# list L2 and has again the corresponding indices a, b, and c. The
# function returns the pair of these Series.
def create_series(L1, L2):
    s1 = pd.Series(L1, index = list("abc"))
    s2 = pd.Series(L2, index = list("abc"))

    return (s1, s2)

# Gets two Series (s1, s2) as parameters and adds to the first Series
# s1 a new value with index 'd'. The new value is the same # as the
# value in Series s2 with index 'b'. Then deletes the element from s2
# that has index 'b'. Now the first Series should have four values,
# while the second list has only two values. Adding a new element to
# a Series can be achieved by assignment, like with dictionaries.
# Deletion of an element from a Series can be done with the del
# statement.
def modify_series(s1, s2):
    s1['d'] = s2.loc['b']
    del s2['b']

    return (s1, s2)
    
def main():
    list_1 = [1, 3, 5]
    list_2 = [2, 4, 6]

    series_1, series_2 = create_series(list_1, list_2)
    print(f"\nSeries 1:\n{series_1}")
    print(f"\nSeries 2:\n{series_2}")

    mod_series_1, mod_series_2 = modify_series(series_1, series_2)
    print(f"\nModified series 1:\n{mod_series_1}")
    print(f"\nModified series 2:\n{mod_series_2}")

    try:
        print(f"\nAdded series:\n{mod_series_1 + mod_series_2}")
    except Error:
        print("Something went wrong!!")
    
if __name__ == "__main__":
    main()
