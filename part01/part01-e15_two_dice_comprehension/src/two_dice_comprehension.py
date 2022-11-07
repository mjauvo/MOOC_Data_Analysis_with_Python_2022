#!/usr/bin/env python3

# Like the exercise 1.05 two dice, except
# this time uses a list comprehension.
def main():
    die = 6

    # Dice
    D = [(i,j) for i in range (1, die+1)
               for j in range (1, die+1)
               if i+j == 5]

    print(*D, sep="\n")

if __name__ == "__main__":
    main()
