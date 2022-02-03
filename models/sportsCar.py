from .car import Car
class SportsCar(Car):
    """
    inherits Cars properties
    """
    def __init__(self,name):
        Car.__init__(self,name)
    """
    Own version of go
    """
    def go(self):
        self._pos = self._pos*2
        