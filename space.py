# Author: Flavio Medina


import turtle
import random
import time

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUM_STARS = 100
STAR_MIN_LENGTH = 5
STAR_MAX_LENGTH = 10
PLANET_COUNT = 3

def setup_screen():
    """Set up the turtle screen."""
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    turtle.bgcolor("black")
    turtle.colormode(255)
    turtle.speed(0)
    turtle.hideturtle()

def draw_star(length):
    """
    Draw a five-pointed star at current turtle position.
    """
    # Semantic Fix
    # Originally missing correct angle (144 degrees for a 5-pointed star)
    for _ in range(5):
        turtle.forward(length)
        turtle.right(144)
