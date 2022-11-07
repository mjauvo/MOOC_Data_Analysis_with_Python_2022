#!/usr/bin/env python3

# Gets an arbitrary number of lists as parameters
# and returns one list containing all the elements
# from the input lists interleaved.
def interleave(*lists):
    zipped = zip(*lists)
    zipped_list = []

    for tuple in zipped:
        zipped_list.extend(tuple)

    return zipped_list

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
