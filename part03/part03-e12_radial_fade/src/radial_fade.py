#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

"""
Make a program that does fading of an image in radial direction.
As we move away from the centre of the image, the pixels fade to
black.
"""

# Returns coordinate pair (center_y, center_x) of the image
# center. The coordinates might not be integers.
def center(a):
    height, width = a.shape[:2]
    center_y = (height-1)/2
    center_x = (width-1)/2

    return (center_y, center_x)   # note the order: (center_y, center_x)

# Returns for image with width 'w' and height 'h' an array
# with shape (h,w), where the number at index (i,j) gives
# the euclidean distance from the point (i,j) to the center
# of the image.
def radial_distance(a):
    height, width = a.shape[:2]
    center_y, center_x = center(a)
    point_y = np.full((width, height), range(height)).T
    point_x = np.full((height, width), range(width))
    rad_dist = np.sqrt((point_y - center_y)**2 + (point_x - center_x)**2)

    return rad_dist

# Returns a copy of the array a with its elements scaled to
# be in the range [tmin,tmax].
def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    scaled_img = np.interp(a, (a.min(), a.max()), (tmin, tmax))
    return scaled_img

# Takes an image as a parameter and returns an array with
# same height and width filled with values between 0.0 and
# 1.0.
def radial_mask(a):
    rad_mask = scale(1 - radial_distance(a))
    return rad_mask

# Returns the image multiplied by its radial mask.
def radial_fade(a):
    rad_fade = a * radial_mask(a)[:, :, np.newaxis]
    return rad_fade

def main():
    image_file = "src/painting.png"

    try:
        painting = plt.imread(image_file)

        img_Y, img_X = center(painting)
        print(f"Image center: ({img_X}, {img_Y})")

        #print(radial_distance(painting))

        fig, ax = plt.subplots(3,1)
        ax[0].imshow(painting)
        ax[1].imshow(radial_mask(painting))
        ax[2].imshow(radial_fade(painting))
        plt.show()
    except IOError:
        print("\nImage not found!!")

    print(center(painting))

if __name__ == "__main__":
    main()
