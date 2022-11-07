#!/usr/bin/env python3

# Gets two sorted lists L1 and L2 as parameters and returns
# a new sorted list L that has all the elements of L1 and L2.
def merge(L1, L2):
    merged_list = L1 + L2
    merged_length = len(merged_list)

    for i in range(merged_length):
        for j in range(0, merged_length-i-1):
            if merged_list[j] > merged_list[j+1]:
                merged_list[j], merged_list[j+1] = merged_list[j+1], merged_list[j]

    return merged_list

def main():
    list1 = [1,5,9,12]
    list2 = [2,6,10,12,5]

    print(merge(list1, list2))

if __name__ == "__main__":
    main()
