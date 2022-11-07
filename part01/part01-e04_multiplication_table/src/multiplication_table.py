#!/usr/bin/env python3

def main():
    rows = 10
    columns = 10

    # rows
    for i in range(1, rows+1):
        print()
        # columns
        for j in range(1, columns+1):
            print ('{:4d}'.format(i*j), end="")

if __name__ == "__main__":
    main()
