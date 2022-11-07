#!/usr/bin/env python3

# Gets two strings of integers as parameters and returns a list
# of integers, splits the strings into words, converts these words
# to integers and returns a list whose elements are multiplication
# of two integers in the respective positions in the lists.
def transform(s1, s2):
    list1    = (list(map(int, s1.split())))
    list2    = (list(map(int, s2.split())))
    products = []

    for i, j in zip(list1, list2):
        products.append(i*j)

    return products

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
