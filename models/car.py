class Car:
    """
    constructor: creates an instance of the class
    """
    def __init__(self,name):
       self.name = name
       self._pos = 0
       
    """
    Increases the cars position
    rasies an exception if rpm > 7
    """
    def go (self):
        
        self._pos += 1
        
    """
    Returns the cars current position
    """
    def getPos(self):
        return self._pos
    """
    Returns cars rotations per min
    """
    def getRPM(self):
        return self._pos / 10


