class Book:
    pass

first_book = Book()
second_book = Book()
third_book = Book()

first_book.name = 'The Art of Computer Programming'
second_book.name = 'Learning Python'
third_book.name = 'Learning Restful Services In 50 Steps'

print(first_book.name)
print(second_book.name)
print(third_book.name)

print(first_book)
#-------------------------
class MotorBike:
    def __init__(self,speed,name,mfg):
        self.speed=speed
        self.name=name
        self.mfg=mfg

Honda=MotorBike(50,"Honda",1999)

print(Honda.name)
print(Honda.speed)
print(Honda.mfg)
Honda.mfg=1970
print(Honda.mfg)


Ducati=MotorBike(250,"Ducati",2002)
print(Ducati.name)
print(Ducati.speed)
print(Ducati.mfg)
Ducati.mfg=2022
print(Ducati.mfg)
#-----------------------

class Planet:
    def __init__(self): 
        pass


planet1 = Planet()
planet1.name="hik"
print(planet1.name) 
#-----------------------
class Book:
    def __init__(self,name):
        self.name = name

learning_python = Book('Learning Python In 100 Steps')
print(learning_python.name)  # Output: "Learning Python In 100 Steps"
#-----------------------
class Planet:
    def __init__(self, name="Earth",dia=0,speed=0):
        self.name = name
        self.dia=dia
        self.speed=speed
    
planet1 = Planet()
print(planet1.name)  # Output: "Earth"
print(planet1.dia)  
print(planet1.speed)  

planet2 = Planet("Jupiter",999,9988)
print(planet2.name)  # Output: "Jupiter"
print(planet2.dia)  
print(planet2.speed) 
#-----------------------------
class Dimen:
    def __init__(self,length):
        if(length<0):
            self.feet = -1
            self.inches = -1
        else:
            self.feet = length//12
            self.inches = length%12
            

d1=Dimen(2345)
print(d1.feet)
print(d1.inches)

print(f"Feet: {d1.feet} and Inches : {d1.inches}")
#------------------------------------------------
class MotorBike:
    def __init__(self,speed):
        self.speed=speed
    def increase_speed(self,val1):
        self.speed+=val1
    def decresae_speed(self,val2):
        self.speed-=val2

honda=MotorBike(50)
print(honda.speed)
honda.increase_speed(300)
print(honda.speed)
honda.decresae_speed(200)
print(honda.speed)
#------------------------------------------------
class Planet:
    def revolve(self):
        print('revolve')
    def rotate(self):
        print('rotate')
    def rev_rot(self):
        self.revolve()
        self.rotate()


earth=Planet()
# earth.revolve()
# earth.rotate()

earth.rev_rot()
#------------------------------------------------
