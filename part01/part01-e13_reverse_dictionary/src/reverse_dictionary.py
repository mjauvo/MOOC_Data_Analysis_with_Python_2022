#!/usr/bin/env python3

# Creates a Finnish to English dictionary based on an
# English to Finnish dictionary d given as a parameter,
# i.e. changes keys to values and vice versa.
def reverse_dictionary(d):
    reversed_dictionary = {}

    for key in d.keys():
        for value in d[key]:
            if value in reversed_dictionary.keys():
                reversed_dictionary[value].append(key)
            else:
                reversed_dictionary[value] = [key]

    return reversed_dictionary

def main():
    d = {'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print("ORIGINAL:")
    print(d)
    print("REVERSED")
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
