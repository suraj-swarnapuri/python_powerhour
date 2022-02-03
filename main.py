import models


toyoda = models.Car("toyoda")
model3 = models.SportsCar("model3")
toyoda.go()
print(toyoda.getPos())