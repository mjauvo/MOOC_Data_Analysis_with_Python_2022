#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

"""
Write a function to_grayscale that takes an RGB image
(3-dimensional array) and returns a two dimensional
gray-scale image. The conversion to gray-scale should
take a weighted sum of the red, green, and blue values,
and use that as the value of gray.

The first axis is the x, the second is y, and the third
is the color components (red, green, blue). Use the weights
0.2126, 0.7152, and 0.0722 for red, green, and blue, respectively.
These weights are so because the human eye is most sensitive
to green color and least sensitive to blue color.
"""

def to_red(image):
    R_img = image.copy()
    R_img[:, :, (1,2)] = 0

    return R_img

def to_green(image):
    G_img = image.copy()
    G_img[:, :, (0,2)] = 0

    return G_img

def to_blue(image):
    B_img = image.copy()
    B_img[:, :, (0,1)] = 0

    return B_img

def to_grayscale(image):
    image_copy = image.copy()

    R_weight = 0.2126
    G_weight = 0.7152
    B_weight = 0.0722

    R_chan = image_copy[:, :, 0]
    G_chan = image_copy[:, :, 1]
    B_chan = image_copy[:, :, 2]

    grayscale_image = R_chan*R_weight + G_chan*G_weight + B_chan*B_weight
    plt.gray()

    return grayscale_image

def main():
    image_file = "src/painting.png"

    try:
        painting = plt.imread(image_file)

        painting_grayscale = to_grayscale(painting)
        plt.imshow(painting_grayscale)

        painting_red = to_red(painting)
        painting_green = to_green(painting)
        painting_blue = to_blue(painting)

        fig, ax = plt.subplots(3, 1)
        ax[0].imshow(painting_red)
        ax[1].imshow(painting_green)
        ax[2].imshow(painting_blue)
        plt.show()
    except IOError:
        print("Image not found !!")

if __name__ == "__main__":
    main()
