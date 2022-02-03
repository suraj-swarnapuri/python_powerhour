from .car import Car
class SportsCar(Car):
    def __init__(self,name):
        Car.__init__(self,name)
    def go(self):
        self._pos = self._pos*2
        