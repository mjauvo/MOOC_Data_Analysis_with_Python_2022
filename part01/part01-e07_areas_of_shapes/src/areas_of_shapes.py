#!/usr/bin/env python3

import math

def triangle():
    "This function calculates the area of a triangle."
    base = float(input("Give base of the triangle: "))
    height = float(input("Give height of the triangle: "))

    print (f"The area is {base*height/2}")

def rectangle():
    "This function calculates the area of a rectangle."
    width = float(input("Give width of the rectangle: "))
    height = float(input("Give height of the rectangle: "))

    print (f"The area is {width*height}")

def circle():
    "This function calculates the area of a circle."
    radius = float(input("Give radius of the circle: "))

    print (f"The area is {math.pi * radius**2}")

def main():
    while True:
        answer = input("\nChoose a shape (triangle, rectangle, circle): ")

        if answer == "triangle":
            triangle()
        elif answer == "rectangle":
            rectangle()
        elif answer == "circle":
            circle()
        elif answer == "":
            break
        else:
            print ("Unknown shape!")


if __name__ == "__main__":
    main()
