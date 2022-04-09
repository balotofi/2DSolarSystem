# binary_star_system.py

from turtle import position
from solarsystem import SolarSystem, Sun, Planet 

solar_system = SolarSystem(width=1400, height=900)

sun_1 = Sun(
    solar_system, 
    mass=10_000, 
    position=(-200,0),
    velocity=(0,3.5),
)

sun_2 = Sun(
    solar_system, 
    mass=10_000, 
    position=(200,0),
    velocity=(0,-3.5),
)

planets = (
    Planet(
    solar_system, 
    mass=20,
    position=(50,0), 
    velocity=(0,11),
    ),
    Planet(
        solar_system,
        mass=3,
        position=(-350,0),
        velocity=(0, -11),
    ),
    Planet(
        solar_system,
        mass=1,
        position=(0,200),
        velocity=(-2, -7),
    ),
)

while True:
    # solar_system.acceleration_due_to_gravity(sun, earth)
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()