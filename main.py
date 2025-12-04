#!/bin/python3
from p5 import *
from make_planet import make_planet


# Draw the Sun

def draw_sun():
    fill(255, 255, 0)  # Yellow
    ellipse(width / 2, height / 2, 100, 100)

# Draw Orbits

def draw_orbits():
    no_fill()
    stroke(255)

    ellipse(width / 2, height / 2, mercury['orbit'], mercury['orbit'])
    ellipse(width / 2, height / 2, venus['orbit'], venus['orbit'])
    ellipse(width / 2, height / 2, earth['orbit'], earth['orbit'])
    ellipse(width / 2, height / 2, mars['orbit'], mars['orbit'])
    ellipse(width / 2, height / 2, jupiter['orbit'], jupiter['orbit'])
    ellipse(width / 2, height / 2, saturn['orbit'], saturn['orbit'])
    ellipse(width / 2, height / 2, uranus['orbit'], uranus['orbit'])
    ellipse(width / 2, height / 2, neptune['orbit'], neptune['orbit'])



# Draw Planets

def draw_planets():
    for planet in (mercury, venus, earth, mars, jupiter, saturn, uranus, neptune):
        make_planet(
            planet["colour"],
            planet["orbit"],
            planet["size"],
            planet["speed"]
        )



# Load Planet Data

def load_planets():
    global mercury, venus, earth, mars, jupiter, saturn, uranus, neptune

    # Mercury is hardcoded
    mercury = {
        'name': 'Mercury',
        'colour': Color(165, 42, 42),
        'size': 15,
        'orbit': 150,
        'speed': 1,
        'info': 'The smallest and fastest planet.'
    }

    # Load CSV data
    with open('planets.csv') as f:
        lines = f.read().splitlines()

    # Venus
    planet = lines[2].split(',')
    venus = {
        'name': planet[0],
        'colour': Color(int(planet[1]), int(planet[2]), int(planet[3])),
        'size': int(planet[4]),
        'orbit': int(planet[5]),
        'speed': float(planet[6]),
        'info': planet[7]
    }

    # Earth
    planet = lines[3].split(',')
    earth = {
        'name': planet[0],
        'colour': Color(int(planet[1]), int(planet[2]), int(planet[3])),
        'size': int(planet[4]),
        'orbit': int(planet[5]),
        'speed': float(planet[6]),
        'info': planet[7]
    }

    # Mars
    planet = lines[4].split(',')
    mars = {
        'name': planet[0],
        'colour': Color(int(planet[1]), int(planet[2]), int(planet[3])),
        'size': int(planet[4]),
        'orbit': int(planet[5]),
        'speed': float(planet[6]),
        'info': planet[7]
    }

    # Jupiter
    planet = lines[5].split(',')
    jupiter = {
        'name': planet[0],
        'colour': Color(int(planet[1]), int(planet[2]), int(planet[3])),
        'size': int(planet[4]),
        'orbit': int(planet[5]),
        'speed': float(planet[6]),
        'info': planet[7]
    }

    # Saturn
    planet = lines[6].split(',')
    saturn = {
        'name': planet[0],
        'colour': Color(int(planet[1]), int(planet[2]), int(planet[3])),
        'size': int(planet[4]),
        'orbit': int(planet[5]),
        'speed': float(planet[6]),
        'info': planet[7]
    }

    # Uranus
    planet = lines[7].split(',')
    uranus = {
        'name': planet[0],
        'colour': Color(int(planet[1]), int(planet[2]), int(planet[3])),
        'size': int(planet[4]),
        'orbit': int(planet[5]),
        'speed': float(planet[6]),
        'info': planet[7]
    }

    # Neptune
    planet = lines[8].split(',')
    neptune = {
        'name': planet[0],
        'colour': Color(int(planet[1]), int(planet[2]), int(planet[3])),
        'size': int(planet[4]),
        'orbit': int(planet[5]),
        'speed': float(planet[6]),
        'info': planet[7]
    }



# Setup

def setup():
    size(400, 400)
    load_planets()



# Draw Loop

def draw():
    background(0)
    no_stroke()
    draw_sun()
    draw_orbits()
    draw_planets()


# Mouse Click Event

def mouse_pressed():

    pixel_colour = Color(get(mouse_x, mouse_y)).hex

    for planet in (mercury, venus, earth, mars, jupiter, saturn, uranus, neptune):
        if pixel_colour == planet["colour"].hex:
            print(planet["name"])
            print(planet["info"])
            break


run(frame_rate=60)
