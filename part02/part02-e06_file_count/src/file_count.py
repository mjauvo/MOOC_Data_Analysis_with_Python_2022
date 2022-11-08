#!/usr/bin/env python3

import sys

# Gets a filename as parameter and returns a triple of
# numbers. Reads the file, counts the number of lines,
# words, and characters in the file, and returns a triple
# with these counts in this order.
def file_count(filename):
    line_count = 0
    word_count = 0
    char_count = 0

    with open(filename) as file:
        for line in file:
            line_count += 1
            word_count += len(line.split())
            char_count += len(line)

    return (line_count, word_count, char_count)

def main():
    for file in sys.argv[1:]:
        line_count, word_count, char_count = file_count(file)
        print(f"{line_count}\t{word_count}\t{char_count}\t{file}")

if __name__ == "__main__":
    main()
