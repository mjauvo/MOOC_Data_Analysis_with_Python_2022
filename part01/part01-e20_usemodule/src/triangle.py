"""Module which contains functions for calculating hypothenuse and area of a triangle"""
from math import sqrt

__author__ = "Markus Auvo"
__version__ = "1.0"

def hypothenuse(side1, side2):
    """Returns the side of the hypothenuse when given the sides of two other sides of a right-angled triangle."""
    return sqrt(pow(side1, 2) + pow(side2, 2))

def area(side1, side2):
    """Returns the area of the right-angled triangle, when two sides, perpendicular to each other, are given as parameters"""
    return side1 * side2 / 2