#!/bin/python3
from p5 import *
from make_planet import make_planet

# -----------------------------------------
# PLANETS LIST
# Format: (colour(R,G,B), orbit_size, planet_size, speed)
# -----------------------------------------

planets = [
    # Planets List - David Sims
    ((0, 0, 255), 340, 22, 0.4),      # Neptune
    ((200, 200, 200), 400, 12, 0.25), # Pluto

    # Planets List - Done by Farzana Happy, ID# 301340971
    ((0, 100, 255), 200, 20, 1.0),    # Earth
    ((210, 180, 140), 260, 30, 0.7),  # Saturn
    ((80, 180, 255), 300, 24, 0.5),   # Uranus
]

def draw_sun():
    fill(255, 255, 0)  # Yellow
    ellipse(width / 2, height / 2, 100, 100)

def draw_orbit():
    no_fill()
    stroke(100)
    for _, orbit, _, _ in planets:
        ellipse(width / 2, height / 2, orbit, orbit)

def draw_planets():
    for colour, orbit, size, speed in planets:
        make_planet(colour, orbit, size, speed)

def setup():
    size(400, 400)

def draw():
    background(0)
    no_stroke()
    draw_sun()
    # draw_orbit()   # Optional
    draw_planets()

def mouse_pressed():
    pixel_colour = Color(get(mouse_x, mouse_y)).hex

run(frame_rate=60)
