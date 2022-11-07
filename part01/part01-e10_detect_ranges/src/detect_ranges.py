#!/usr/bin/env python3

# Gets a list L of integers as a parameter, sorts the list, and
# transform the list into another list where pairs are used for
# all the detected intervals.
# 
# So 3,4,5,6 is replaced by the pair (3,7). Numbers that are not
# part of any interval result just single numbers. The resulting
# list consists of these numbers and pairs, separated by commas.
def detect_ranges(L):
    sorted_list = sorted(L)
    list_with_ranges = []
    index = 0

    while sorted_list:
        if len(sorted_list) == 1:
            list_with_ranges.append(sorted_list[0])
            sorted_list.pop(0)
        elif sorted_list[index+1] == sorted_list[index] + 1:
            index += 1
            if index == len(sorted_list)-1:
                list_with_ranges.append((sorted_list[0], sorted_list[index]+1))
                sorted_list = []
        else:
            if index == 0:
                list_with_ranges.append(sorted_list[0])
                sorted_list.pop(0)
            else:
                list_with_ranges.append((sorted_list[0], sorted_list[index]+1))
                del sorted_list[:index+1]
                index = 0

    return list_with_ranges

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
