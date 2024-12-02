from sense_hat import SenseHat
import time
import math

sense = SenseHat()

#Define colors
orange = [255, 165, 0]
blue = [0, 0, 255]
black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]

#Define images and animations
spider_image =[
red, white, white, white, white, white, white, red,
 white, red, red, white, white, red, red, white,
 white, white, white, red, red,  white, white, white,
red, red, red, red, red, red, red, red,
 white, white, white, red, red,  white, white, white,
 white, red, red, red, red, red, red,  white,
red, white, white,blue, blue,  white, white, red,
red,  white, white, white, white, white, white, red
]

def idle():
    sense.clear(orange)

def manual():
    sense.clear(white)

def startup():
	sense.clear(blue)

def shutdown():
	sense.clear(red)

def auto():
    sense.set_pixels(spider_image)

def devmode():
    sense.clear(black) # placeholder

def disable():
    sense.clear(black)

def arrow_left():
    """
    Displays an arrow pointing to the left on the Sense HAT LED matrix.
    """
    arrow_left = [
        O, O, O, R, O, O, O, O,
        O, O, R, R, O, O, O, O,
        O, R, R, R, R, R, R, R,
        R, R, R, R, R, R, R, R,
        O, R, R, R, R, R, R, R,
        O, O, R, R, O, O, O, O,
        O, O, O, R, O, O, O, O,
        O, O, O, O, O, O, O, O
    ]
    sense.set_pixels(arrow_left)

def arrow_right():
    """
    Displays an arrow pointing to the right on the Sense HAT LED matrix.
    """
    arrow = [
        O, O, O, O, R, O, O, O,
        O, O, O, O, R, R, O, O,
        R, R, R, R, R, R, R, O,
        R, R, R, R, R, R, R, R,
        R, R, R, R, R, R, R, O,
        O, O, O, O, R, R, O, O,
        O, O, O, O, R, O, O, O,
        O, O, O, O, O, O, O, O
    ]
    sense.set_pixels(arrow)

def arrow_up():
    """
    Displays an arrow pointing upwards on the Sense HAT LED matrix.
    """
    arrow = [
        O, O, O, O, R, O, O, O,
        O, O, O, R, R, R, O, O,
        O, O, R, R, R, R, R, O,
        O, R, R, R, R, R, R, R,
        O, O, O, R, R, R, O, O,
        O, O, O, R, R, R, O, O,
        O, O, O, R, R, R, O, O,
        O, O, O, R, R, R, O, O
    ]
    sense.set_pixels(arrow)