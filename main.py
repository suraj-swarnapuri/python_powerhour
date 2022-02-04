import models
from models import Car
from models import SportsCar

"""
classes
inheritence
polymorphism
encapsulation
error handling
"""

def main():
    print("hello world")

    # make a new Car by calling Car.__init__(name)
    c = Car("honda")
   
    
    t = SportsCar("tesla")
    

    for i in range(0,10):
        try: 
            c.go()
            t.go()
        except Exception as e:
            print(e)
            break

        print(c.modelName,": ",c.getPos(), ":", c.getRPM())
        print(t.modelName,": ",t.getPos(), ":", t.getRPM())







if __name__ == "__main__":
    main()