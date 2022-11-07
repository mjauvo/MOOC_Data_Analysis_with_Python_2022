#!/usr/bin/env python3

# Takes a list L of positive integers as parameters and returns
# a string with an equation of the sum of the elements.
def sum_equation(L):
    if len(L) == 0:
        return "0 = 0"
    else:
        string_L = [str(i) for i in L]
        equation = " + ".join(string_L)
        equation += " = %i" % sum(L)

        return equation

def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
