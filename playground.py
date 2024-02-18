#*args: Many Positional Arguments.
#def add(*args):
#    print(args[0])
#    sum = 0
#    for n in args:
#        sum += n
#    return sum
#print(add(3, 5, 6, 2, 1, 7, 4, 3))
#**kwargs: Many Keyword Arguments.
def calculate(n,**kwargs):
    #for key,value in kwargs.items():
    #    print(key)
    #    print(value)
    #print(type(kwargs))
    #print(kwargs)
    n+= kwargs["add"]
    n*= kwargs["multiply"]
    print(n)
#calculate( 2, add = 3, multiply = 5)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#**kwargs: Many Keyword Arguments.
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
class Car:
    def __init__(self,**kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")
my_car = Car(make="Nissan", model="GT-R")
#When I'm initializing.All you see is**kw.
print(my_car.make)
print(my_car.model)
love_car = Car(make="Jeep", model="jeep 4x4",colour="Black",seats=5)
print(love_car.make)
print(love_car.model)
print(love_car.colour)
print(love_car.seats)
######################
######################




