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

    # Planets List - Done by Maryam Khan, ID# 301371688
    ((255, 200, 50), 160, 16, 1.2),   # Venus
    ((255, 80, 50), 240, 14, 0.8),    # Mars
    ((180, 180, 180), 120, 10, 1.6),  # Mercury
    ((230, 150, 80), 280, 40, 0.6),   # Jupiter

    # Moon List - Isaiah Newman
    ((180, 180, 180), 40, 6, 2.0)   # Luna

]

def draw_sun():
    fill(255, 255, 0)  # Yellow
    ellipse(width / 2, height / 2, 100, 100)

def draw_orbit():
    no_fill()
    stroke(100)
    for i, (_, orbit, _, _) in enumerate(planets):
        if i == len(planets) - 1:  # skip Moon
            continue
        ellipse(width / 2, height / 2, orbit, orbit)

def draw_planets():
    earth_x = earth_y = None

    for i, (colour, orbit, size, speed) in enumerate(planets):
        # Only skip drawing the Moon for Sun-centered orbit
        if colour == (180, 180, 180) and i == len(planets) - 1:
            # This is the Moon; skip Sun orbit
            pass
        else:
            make_planet(colour, orbit, size, speed)

        # Store Earth's position for the Moon
        if colour == (0, 100, 255):  # Earth
            angle = radians((frame_count * speed) % 360)
            earth_x = width/2 + (orbit/2) * cos(angle)
            earth_y = height/2 + (orbit/2) * sin(angle)

    # Draw Moon orbiting Earth
    if earth_x is not None and earth_y is not None:
        moon_colour, moon_orbit, moon_size, moon_speed = planets[-1]  # Last in list is Moon
        moon_angle = radians((frame_count * moon_speed) % 360)
        moon_x = earth_x + moon_orbit * cos(moon_angle)
        moon_y = earth_y + moon_orbit * sin(moon_angle)
        fill(*moon_colour)
        ellipse(moon_x, moon_y, moon_size, moon_size)

def setup():
    size(400, 400)

def draw():
    background(0)
    no_stroke()
    draw_sun()
    draw_orbit()   # Optional
    draw_planets()

def mouse_pressed():
    pixel_colour = Color(get(mouse_x, mouse_y)).hex

run(frame_rate=60)
