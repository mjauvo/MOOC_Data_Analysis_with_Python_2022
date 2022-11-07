#!/usr/bin/env python3

def main():
    die_1 = 6
    die_2 = 6

    # Die 1
    for i in range(1, die_1+1):
        # Die 2
        for j in range(1, die_2+1):
            if (i + j) == 5:
                print(f"({i}, {j})")

if __name__ == "__main__":
    main()
