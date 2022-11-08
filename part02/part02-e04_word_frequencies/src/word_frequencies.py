#!/usr/bin/env python3

import string

# Gets a filename as a parameter and returns # a dict
# with the word frequencies.In the dictionary the keys
# are the words and the corresponding values are the
# number of times that word occurred in the file specified
# by the function parameter
def word_frequencies(filename):
    frequency_dictionary = {}

    with open(filename) as file:
        for line in file:
            for word in line.split():
                stripped_word = word.strip(string.punctuation)

                if stripped_word not in frequency_dictionary:
                    frequency_dictionary[stripped_word] = 1
                else:
                    frequency_dictionary[stripped_word] += 1

    return frequency_dictionary

def main():
    filename = "src/alice.txt"
    print(word_frequencies(filename))

if __name__ == "__main__":
    main()
