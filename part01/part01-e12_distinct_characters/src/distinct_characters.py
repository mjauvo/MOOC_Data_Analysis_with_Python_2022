#!/usr/bin/env python3

# Gets a list L of strings as a parameter and returns a dictionary
# whose keys are the strings of the input list and the corresponding
# values are the numbers of distinct characters in the key.
def distinct_characters(L):
    dictionary = {}

    for word in L:
        dictionary[word] = len(set(word))

    return dictionary

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
