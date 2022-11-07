#!/usr/bin/env python3

def is_positive(x):
    return x > 0

# Gets a list L of numbers as a parameter, and returns
# a list with negative numbers and zero filtered out.
def positive_list(L):
    positives = list(filter(is_positive, L))
    return positives

def main():
    L = [2,-2,0,1,-7]
    print(positive_list(L))

if __name__ == "__main__":
    main()
