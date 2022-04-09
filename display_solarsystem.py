# display_solarsystem.py

from solarsystem import Planet, SolarSystem, Sun

solar_system = SolarSystem(width=1000, height=640)

sun = Sun(
    solar_system, 
    mass=10_000, 
    velocity=(0,0)
)

planets = (
    Planet(
    solar_system, 
    mass=1, 
    position=(-600, 0),
    velocity=(0,3),
    ),
    Planet(
        solar_system,
        mass=1,
        position=(-350, 0),
        velocity=(0, 1),
    ),
    Planet(
        solar_system,
        mass=2,
        position=(-270, 0),
        velocity=(0, 7),
    ),
)

while True:
    # solar_system.acceleration_due_to_gravity(sun, earth)
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()