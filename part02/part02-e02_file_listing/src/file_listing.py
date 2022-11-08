#!/usr/bin/env python3

import re

# Loads the file 'src/listing.txt' and returns a list
# of tuples (size, month, day, hour, minute, filename)
# using regular expression.
def file_listing(filename="src/listing.txt"):
    tuple_list = []
    regex = r"\S+\s\d\s\w+\s\S+\s+(\d+)\s([A-Za-z]{3})\s+(\d{1,})\s(\d{2}):(\d{2})\s(.+)"

    with open(filename) as file:
         for line in file:
            tuple = re.findall(regex, line)
            modified_tuple = (int(tuple[0][0]), tuple[0][1], int(tuple[0][2]), int(tuple[0][3]), int(tuple[0][4]), tuple[0][5])
            tuple_list.append(modified_tuple)

    return tuple_list

def main():
    print(file_listing())

if __name__ == "__main__":
    main()
