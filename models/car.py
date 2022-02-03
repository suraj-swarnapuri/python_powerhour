class Car:
    
    def __init__(self,name):
       self._name = name
       self._pos = 0 
    def go (self):
        self._pos += 1
    def getPos(self):
        return self._pos


