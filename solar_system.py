class System:
    
    def __init__(self):
        self.bodies = []

    def add(self, body):
        self.bodies.append(body)

    def total_mass(self):
        total = 0
        for body in self.bodies:
            total += body.mass
            return total

class Body(System):

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

class Planet(Body):

    def __init__(self, name, mass, day, year):
        super().__init__(name, mass)
        self.day = day
        self.year = year

class Star(Body):

    def __init__(self, name, mass, type):
        super().__init__(name, mass)
        self.type = type

class Moon(Body):

    def __init__(self, name, mass, month, planet):
        super().__init__(name, mass)
        self.month = month
        self.planet = planet

earth = Planet("Earth", 59720, 24, 365)
sun = Star("Sun", 333000, "G-type")
moon = Moon("Moon", 7347, 30, "Earth")

solarsystem = System()


solarsystem.add(earth)
solarsystem.add(sun)
solarsystem.add(moon)

print(solarsystem.bodies)
print(solarsystem.total_mass())