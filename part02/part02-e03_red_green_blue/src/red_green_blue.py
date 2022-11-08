#!/usr/bin/env python3

import re

# Reads the file 'src/rgb.txt', removes the irrelevant
# first line of the file, and returns a list of strings
# having four fields separated by a single tab character
# (\t) using regular expressions to do this.
def red_green_blue(filename="src/rgb.txt"):
    string_list = []
    regex  = r"\s*(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})\s+(.*)"

    with open(filename) as file:
        next(file)
        for line in file:
            matched_string = re.match(regex, line)
            modified_string = f"{matched_string.group(1)}\t{matched_string.group(2)}\t{matched_string.group(3)}\t{matched_string.group(4)}"
            string_list.append(modified_string)

    return string_list

def main():
    print(red_green_blue())

if __name__ == "__main__":
    main()
