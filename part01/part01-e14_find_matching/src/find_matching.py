#!/usr/bin/env python3

# Gets a list L of strings and a search string pattern as
# parameters and returns the indices to those elements in
# the input list that contain the search string.
def find_matching(L, pattern):
    indices = []

    for index, element in enumerate(L):
        if element.find(pattern) > -1:
            indices.append(index)

    return indices


def main():
    L = ["jedi", "may", "the", "jedi", "force", "be", "with", "you", "jedi"]
    print(find_matching(L, "edi"))

if __name__ == "__main__":
    main()
