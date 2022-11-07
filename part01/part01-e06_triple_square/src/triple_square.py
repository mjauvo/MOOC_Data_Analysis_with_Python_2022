#!/usr/bin/env python3

def triple(x):
    "This function multiplies its parameter by three."
    return x*3

def square(x):
    "This function raises its parameter to the power of two."
    return x**2

def main():
    for i in range(1, 11):
        tr = triple(i)
        sq = square(i)

        if sq <= tr:
            print(f"triple({i})=={tr} square({i})=={sq}")
        else:
            break

if __name__ == "__main__":
    main()
