#!/bin/python3
from p5 import *
from make_planet import make_planet

#Planets List - David Sims
planets = [
    ((0,0,255), 340, 22, 0.4), #Neptune
    ((200,200,200),400,12,0.25) #Pluto
]

def draw_sun():
    fill(255, 255, 0)  # Yellow
    ellipse(width / 2 , height / 2, 100, 100)


# draw_orbits function
def draw_orbit():
    no_fill()
    stroke(100) #This can show a greyish orbit - DS
    for _, orbit, _, in planets:
        ellipse(width / 2, height / 2, orbit, orbit)


# draw_planets function

def draw_planets():
    for colour, orbit, size, speed, in planets:
        make_planet(colour, orbit, size, speed) #creation of planet -ds

# load_planets function
  
def setup():
    # Put code to run once here
    size(400, 400)

  
def draw():
    # Put code to run every frame here
    background(0)
    no_stroke()
    draw_sun()
    draw_planets() #draw planets -ds


def mouse_pressed():
    # Put code to run when the mouse is pressed here
    pixel_colour = Color(get(mouse_x, mouse_y)).hex  # Here the RGB value is converted to Hex so it can be used in a string comparison later

  
run(frame_rate=60)

