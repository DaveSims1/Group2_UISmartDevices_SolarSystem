from p5 import *
from make_planet import make_planet

def setup():
    size(400, 400)

def draw():
    background(0)

    # Test drawing a single planet
    test_colour = (0, 100, 255)   # Earth blue
    test_orbit = 150              # Distance from sun
    test_size = 30                # Planet size
    test_speed = 1.0              # Rotation speed

    # Draw sun
    fill(255, 255, 0)
    ellipse(width/2, height/2, 100, 100)

    # Call the planet function you want to test
    make_planet(test_colour, test_orbit, test_size, test_speed)

run()
