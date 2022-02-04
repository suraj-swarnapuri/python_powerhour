class Car:
    """
    constructor: creates an instance of the class
    """
    def __init__(self,name):
       self.modelName = name
       self._pos = 1
       
    """
    Increases the cars position
    rasies an exception if rpm > 7
    """
    def go (self):
        try:
            self.validateSpeed()
        except Exception as e:
            raise(e)
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
    
    def validateSpeed(self):
        if self.getRPM() > 7:
            raise Exception("Slow down bucko")



"""
How to create a function:
def <name of the function> ( ...param ):
    ->
"""
