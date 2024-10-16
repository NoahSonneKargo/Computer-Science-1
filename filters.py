
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 1: In this project I am a trying to create different outcomes for the same picture
by manipulating the colors red, green and blue.
@author: Noah Sonne Kargo
"""

import math
import random

default_image_name = 'houseScenery.jpg'


def grayscale(red, green, blue):
    total = red + green + blue
    avg = total // 3
    return avg, avg, avg


def colorblind(red, green, blue):
    avg = (red + green) // 2
    return avg, avg, blue


def posterize(red, green, blue, options=5):
    range = 255 // options

    red_posterize = (red // range) * range
    green_posterize = (green // range) * range
    blue_posterize = (blue // range) * range

    return red_posterize, green_posterize, blue_posterize


def lighter(red, green, blue):
    max_increase_red = 255 - red
    max_increase_green = 255 - green
    max_increase_blue = 255 - blue

    increase_red = red + max_increase_red * 45 // 100
    increase_green = green + max_increase_green * 45 // 100
    increase_blue = blue + max_increase_blue * 45 // 100

    new_red = min(increase_red, 255)
    new_green = min(increase_green, 255)
    new_blue = min(increase_blue, 255)

    return new_red, new_green, new_blue


def black_white(red, green, blue):
    sum = red + green + blue
    white = sum // 382
    return white * 255, white * 255, white * 255


def tiedye(red, green, blue):
    last_digits_red = red % 100
    last_digits_green = green % 100
    last_digits_blue = blue % 100

    new_red = last_digits_red * 5
    new_green = last_digits_green * 5
    new_blue = last_digits_blue * 5

    return new_red, new_green, new_blue


# I wanted to experiment with whether I could make it darker in some ares using the height and the value y

def my_filter(red, green, blue, x, y, width, height):

# Starting out with the change being 0
    change = 0

# Here I check whether the pixel is in the upper half of the lower half of the picture
    if y < height / 2:
        change = 100  # It will be brighter in the upper half
    else:
        change = -100  # It will be darker in the lower half

# Changing the old value into the new and ensuring that the new value will stay in between 0-255
    new_red = max(0, min(255, red + change))
    new_green = max(0, min(255, green + change))
    new_blue = max(0, min(255, blue + change))

# Returning the new values
    return new_red, new_green, new_blue


""" Write no new code below here """

""" Here be dragons """

""" Don't Change this code """

def main():
    import elon_image
    elon_image.main(default_image_name)

if __name__ == '__main__':
    main()
