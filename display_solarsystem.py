# display_solarsystem.py

from solarsystem import SolarSystem, Sun

solar_system = SolarSystem(width=1000, height=640)
sun = Sun(solar_system, mass=10_000)
sun.draw()

# Temporary lines
import turtle
turtle.done()