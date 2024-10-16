#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 13:46:52 2020
@author: rmattfeld

Modified on Tue Feb 14 16:29:00 2023
@author: sosborne3
"""

from PIL import Image
import filters
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

image = None


def load_image(file):
    global image 
    image = Image.open(file)
    

def get_width():
    global image
    return image.width


def get_height():
    global image
    return image.height


def do_inversion():
    global image
    for x in range(get_width()):
        for y in range(get_height()):
            intensities = image.getpixel((x,y))
            new_pixel = filters.invert(intensities[0], intensities[1], intensities[2])
            image.putpixel((x,y),(new_pixel[0],new_pixel[1],new_pixel[2]))


def make_gray():
    global image
    for x in range(get_width()):
        for y in range(get_height()):
            intensities = image.getpixel((x,y))
            new_pixel = filters.grayscale(intensities[0], intensities[1], intensities[2])
            image.putpixel((x,y),(new_pixel[0],new_pixel[1],new_pixel[2]))

def do_black_white():
    global image
    for x in range(get_width()):
        for y in range(get_height()):
            intensities = image.getpixel((x,y))
            new_pixel = filters.black_white(intensities[0], intensities[1], intensities[2])
            image.putpixel((x,y),(new_pixel[0],new_pixel[1],new_pixel[2]))

def lighten_up():
    global image
    for x in range(get_width()):
        for y in range(get_height()):
            intensities = image.getpixel((x,y))
            new_pixel = filters.lighter(intensities[0], intensities[1], intensities[2])
            image.putpixel((x,y),(new_pixel[0],new_pixel[1],new_pixel[2]))


def do_posterization():
    global image
    for x in range(get_width()):
        for y in range(get_height()):
            intensities = image.getpixel((x,y))
            new_pixel = filters.posterize(intensities[0], intensities[1], intensities[2])
            image.putpixel((x,y),(new_pixel[0],new_pixel[1],new_pixel[2]))


def do_tiedye():
    global image
    for x in range(get_width()):
        for y in range(get_height()):
            intensities = image.getpixel((x,y))
            new_pixel = filters.tiedye(intensities[0], intensities[1], intensities[2])
            image.putpixel((x,y),(new_pixel[0],new_pixel[1],new_pixel[2]))


def do_colorblind():
    global image
    for x in range(get_width()):
        for y in range(get_height()):
            intensities = image.getpixel((x,y))
            new_pixel = filters.colorblind(intensities[0], intensities[1], intensities[2])
            image.putpixel((x,y),(new_pixel[0],new_pixel[1],new_pixel[2]))

def do_my_filter():
    global image
    for x in range(get_width()):
        for y in range(get_height()):
            intensities = image.getpixel((x,y))
            new_pixel = filters.my_filter(intensities[0], intensities[1], intensities[2],
                                          x,y,get_width(), get_height())
            image.putpixel((x,y),(new_pixel[0],new_pixel[1],new_pixel[2]))


def set_red(x, y, intensity):
    global image 
    intensities = image.getpixel((x,y))
    if len(intensities) == 4:
        image.putpixel((x,y),(intensity,intensities[1],intensities[2],intensities[3]))
    elif len(intensities) == 3:
        image.putpixel((x,y),(intensity,intensities[1],intensities[2]))    
    else:
        print('Invalid image given. Please try another image.')
    

def set_blue(x, y, intensity):
    global image 
    intensities = image.getpixel((x,y))
    if len(intensities) == 4:
        image.putpixel((x,y),(intensities[0],intensities[1],intensity,intensities[3]))
    elif len(intensities) == 3:
        image.putpixel((x,y),(intensities[0],intensities[1],intensity))    
    else:
        print('Invalid image given. Please try another image.')
    
    
def set_green(x, y, intensity):
    global image 
    intensities = image.getpixel((x,y))
    if len(intensities) == 4:
        image.putpixel((x,y),(intensities[0],intensity,intensities[2],intensities[3]))
    elif len(intensities) == 3:
        image.putpixel((x,y),(intensities[0],intensity,intensities[2]))    
    else:
        print('Invalid image given. Please try another image.')
 

def set_alpha(x, y, intensity):
    global image 
    intensities = image.getpixel((x,y))
    if len(intensities) == 4:
        image.putpixel((x,y),(intensities[0],intensities[1],intensities[2],intensity))
    elif len(intensities) == 3:
        image.putpixel((x,y),(intensities[0],intensities[1],intensities[2]))    
    else:
        print('Invalid image given. Please try another image.')
    

def set_pixel(x, y, r, g, b, a=255):
    global image
    intensities = image.getpixel((x,y))
    if len(intensities) == 4:
        image.putpixel((x,y),(r,g,b,a))
    elif len(intensities) == 3:
        image.putpixel((x,y),(r,g,b))    
    else:
        print('Invalid image given. Please try another image.')
    

def get_red(x, y):
    global image 
    intensities = image.getpixel((x,y))
    return intensities[0]
    

def get_blue(x, y):
    global image 
    intensities = image.getpixel((x,y))
    return intensities[2]
    

def get_green(x, y):
    global image 
    intensities = image.getpixel((x,y))
    return intensities[1]
    

def get_alpha(x, y):
    global image 
    intensities = image.getpixel((x,y))
    if len(intensities) == 4:
        return intensities[3]
    else:
        return -1
    

def draw():
    image.show()
    

def save(filename):
    global image
    image = image.save(filename)
    

# Do not change any of the code below!
def main(default_filename):
    go_time = True
  
    image_name = input('Hit enter to use the default image, or\ntype the image name you want to use: ')

    if image_name == '':
        image_name = default_filename

    load_image(image_name)
    while go_time:
        choice =int(input('Which filter would you like to use?\n'+
                      '1: Grayscale:\n2: Colorblind \n3: Posterize\n4: Lighter\n'+
                      '5: Black and White\n6: Tie Dye\n7: My Filter\n'+
                      '8: Reload image\n9: Quit\n'))

        if choice == 1:
            make_gray()
            draw()
        elif choice ==2:
            do_colorblind()
            draw()
        elif choice == 3:
            do_posterization()
            draw()
        elif choice == 4:
            lighten_up()
            draw()
        elif choice == 5:
            do_black_white()
            draw()
        elif choice == 6:
            do_tiedye()
            draw()
        elif choice == 7:
            do_my_filter()
            draw()
        elif choice == 8:
            load_image(image_name)
        else:
            go_time = False

    
if __name__ == '__main__':
    main()
