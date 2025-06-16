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

def random_star():
    """
    Draw a single star at a random location, orientation, and size.
    """
    x = random.randint(-SCREEN_WIDTH // 2, SCREEN_WIDTH // 2)
    y = random.randint(-SCREEN_HEIGHT // 2, SCREEN_HEIGHT // 2)
    size = random.randint(STAR_MIN_LENGTH, STAR_MAX_LENGTH)
    angle = random.randint(0, 360)
    
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(angle)

    # Use random colors
    turtle.color("white", random.choice(["white", "yellow", "lightblue", "lightyellow"]))
    turtle.pendown()
    draw_star(size)

def draw_world(x, y, radius, fill_color):
    """
    Draw a filled circle to represent a planet or moon.
    """
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.setheading(0)
    turtle.color(fill_color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(radius)
    turtle.end_fill()

def draw_celestial_bodies():
    """
    Draw the full starry sky: stars and planets with slight delays for effect.
    """
    for _ in range(NUM_STARS):
        random_star()
        turtle.update()
        time.sleep(0.01)  # A bit slows star drawing slightly (adjust as needed)

    # Draw three planets
    for _ in range(PLANET_COUNT):
        x = random.randint(-SCREEN_WIDTH // 2 + 50, SCREEN_WIDTH // 2 - 50)
        y = random.randint(-SCREEN_HEIGHT // 2 + 50, SCREEN_HEIGHT // 2 - 50)
        radius = random.randint(20, 60)
        color = random.choice(["gray", "blue", "green", "red", "purple"])
        draw_world(x, y, radius, color)
        turtle.update()
        time.sleep(0.01)  # A bit slower delay for planets
