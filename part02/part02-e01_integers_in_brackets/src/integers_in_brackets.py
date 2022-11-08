#!/usr/bin/env python3

import re

# Finds from a given string s all integers
# that are enclosed in brackets.
def integers_in_brackets(s):
    regex = r"\[\s*([+-]?\d+)\s*\]"

    integer_list = re.findall(regex, s)
    integer_list = [int(x) for x in integer_list]

    return integer_list

def main():
    s = " afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"
    print(integers_in_brackets(s))

if __name__ == "__main__":
    main()
