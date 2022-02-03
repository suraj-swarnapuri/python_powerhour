import models

"""
classes
inheritence
polymorphism
encapsulation
error handling
"""

toyoda = models.Car("toyoda")
model3 = models.SportsCar("model3")
toyoda.go()
print(toyoda.getPos())