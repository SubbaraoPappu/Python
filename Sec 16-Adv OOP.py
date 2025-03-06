# Define the Fan class
class Fan:
    # Constructor to initialize the fan
    def __init__(self, make, radius, color):
        self.make = make
        self.radius = radius
        self.color = color
        self.speed = 0  # Initial speed is 0
        self.is_on = False  # Fan is initially off
    
    # Method to represent the Fan object as a string
    def __repr__(self):
        return repr((self.make, self.radius, self.color, self.speed, self.is_on))
    
    # Method to switch the fan on
    def switch_on(self):
        self.is_on = True
        self.speed = 3  # Set initial speed to 3
    
    # Method to switch the fan off
    def switch_off(self):
        self.is_on = False
        self.speed = 0  # Reset speed to 0
    
    # Method to increase the fan speed
    def increase_speed(self):
        if self.is_on and self.speed < 5:  # Max speed is 5
            self.speed += 1
    
    # Method to decrease the fan speed
    def decrease_speed(self):
        if self.is_on and self.speed > 0:  # Min speed is 0
            self.speed -= 1
    
# Create a Fan object and test the methods
fan = Fan('Bajaj', 5, 'Green')
print(fan)  # Output: ('Manufacturer 1', 5, 'Green', 0, False)
    
fan.switch_on()
print(fan)  # Output: ('Manufacturer 1', 5, 'Green', 3, True)
    
fan.increase_speed()
print(fan)  # Output: ('Manufacturer 1', 5, 'Green', 4, True)
    
fan.switch_off()
print(fan)  # Output: ('Manufacturer 1', 5, 'Green', 0, False)
#----------------------------------------------------------------
#----------------------------------------------------------------
class Book:
    def __init__(self, id, name, author):
        self.id = id
        self.name = name
        self.author = author
        self.reviews = []

    def __repr__(self):
        return repr( (self.id, self.name, self.author, self.reviews) )
    
    def add_review(self,rv1):
        self.reviews.append(rv1)

book1=Book(123, 'object programming', 'robert')
# book1.reviews=('bad review1','bdr2')

book2=Book(128, 'C  programming', 'David 12')
# book2.reviews=('Good review1','best revie11')
print(book1)
print(book2)

class Review:
    def __init__(self, id, description, rating):
        self.id = id
        self.desc = description
        self.rating = rating
    def __repr__(self):
        return repr((self.id, self.desc, self.rating))

review1 = Review('R01','Bad Reveiw1','2 out5')
print (review1)
review2 = Review('R02','Good Reveiw1','5 out5')
print (review2)

# Now add the review objects to the book objects
#-- reviews on the book object is a list
# the below will only replace the review attribute value 
# but ot does not append
book1.reviews.append(review1) 
print(book1)
#output -->>> (123, 'object programming', 'robert', ('R01', 'Bad Reveiw1', '2 out5'))

book2.reviews.append(review2)
print(book2)
#output -->>> (123, 'object programming', 'robert', ('R02', 'Good Reveiw1', '5 out5'))

# To ovecome this we will create a mehod called add review in book class and call it 
# with the review onject and it will append the reviews list on the book object with the list of given rewiews

book1.add_review(review1)
print(book1)

book2.add_review(review2)
print(book2)

#--------------End of Prog--------------------------------------------------
#--------------Class level inheritance -------------------------------------
class Animal:
    def bark(self):
        print('bark')

an1 = Animal()
an1.bark()

class Pet(Animal):
    def groom(self):
        print('groom')
    
dog=Pet()
dog.bark() #object dog inherits the bark class defined in animal class as the pet class is extending the Animal class
dog.groom()
#--------------End of Prog--------------------------------------------------
#---------------All classes inherigs Object class------------------------
class Book(object):
    def __init__(self, id, name, copies):
        self.id = id
        self.name = name
        self.copies = copies
    
    # Here below __repr__ has been overridden and we gave a special implementation
    # def __repr__(self):
    #     return repr( "I amd xxxxxxxxx")

    # def __repr__(self):
    #     return repr((self.id , self.name, self.copies))

book = Book(1,'b1',90)
print(book)  # Output: <__main__.Book object at some_memory_location>

#--------------End of Prog--------------------------------------------------

#----------------------------------------------------------------
#-----------------Inheritance from 2 objects---------------------
# Amphibian class inheriting from LandAnimal + WildAnimal classes
#----------------------------------------------------------------
class LandAnimal:
    def __init__(self):
        super().__init__()
        self.WalkingSpeed = 5
    
    def increase_walking_speed(self,speed):
        self.WalkingSpeed += speed

class WaterAnimal:
    def __init__(self):
        super().__init__()
        self.SwimmingSpeed = 20
    def increase_swimming_speed(self,speed):
        self.SwimmingSpeed += speed

class Amphian(LandAnimal, WaterAnimal):
    def __init__(self):
        super().__init__()
    
    def __repr__(self):
        return repr(('From Amphibian',self.WalkingSpeed, self.SwimmingSpeed))
        

am1=Amphian()
print(am1.SwimmingSpeed)
print(am1.WalkingSpeed)

print(am1)

am1.increase_swimming_speed(30)
am1.increase_walking_speed(30)
print(am1.SwimmingSpeed)
print(am1.WalkingSpeed)


print(am1)
#--------------End of Prog--------------------------------------------------
#----------------------------------------------------------------
#-------------Multiple clases inheritance and -----------------------------
#----------------------------------------------------------------
#TODO: Implement the `start_engine` method to return "Engine started".
class Engine:
    def __init__(self):
        super().__init__()
    def start_engine(self):
        return "Engine Started"

#TODO: Implement `number_of_wheels` method to return number of wheels - 4.
class Wheels:
    def __init__(self):
        super().__init__()
        self.wheels = 4
    def number_of_wheels(self):
        return "4"


#TODO: Make class inherit from Engine & Wheels
#TODO: Implement the `drive` method to return "Car is driving".
class Car(Engine, Wheels): 
    def __init__(self):
        super().__init__()
    def drive(self)    :
        return "Car is Driving"

v1 = Car()
result_start = v1.start_engine()
print(result_start) # Output: "Engine started"

# Test drive
result_drive = v1.drive()
print(result_drive) # Output: "Car is driving"

# Test number of wheels
num_wheels = v1.number_of_wheels()  
print(num_wheels) # Output: 4
#--------------End of Prog--------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
# Understanding Abstract Classes in Python
#----------------------------------------------------------------
# An abstract class serves as a blueprint for other classes. It allows you to 
# define methods that must be created within any child classes built from the 
# abstract class. In other words, an abstract class can contain methods that have no implementation in the base class itself.

#----------------------------------------------------------------
# Notes : 
# 1) Import the abc module and then ABC calss and abstractmenthod
# 2) now define the class and extend the ABC class
# 3) Now mention the abstractmentod before we go an declare the abs methods in the abs class
# 4) Now define all the abstract methods withself and other parmeters as required
# 5) decalss the "pass" as the implementation body onthe class

from abc import ABC, abstractmethod
#this import must be declared for     
class AbstactAnimal(ABC):
    @abstractmethod
    def bark(self):
        pass

class PetAnimal(AbstactAnimal):
    def bark(self):
        print ("Bow owowowowow")

dog=PetAnimal()
dog.bark()
#--------------End of Prog--------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
# Using Template Method Pattern in Object-Oriented Programming (OOP)
#----------------------------------------------------------------
# The objective of this step is to dive into a specific design pattern known 
# as the Template Method Pattern. This pattern is particularly useful when you  
# want to define the structure of an algorithm but allow subclasses to implement 
# specific steps.

# Eg : you are building a class to represent various recipes. There are general 
# steps like “preparing the ingredients,” “following the recipe,” and 
# “cleaning up” that are common to all recipes. However, the specifics of these 
# steps will differ depending on what you’re cooking. 
# 
# This is where the Template Method Pattern comes into play.
#----------------------------------------------------------------
#----------------------------------------------------------------
from abc import ABC, abstractmethod
class AbstractRecipe(ABC):
    def execute(self):
        self.prepare()
        self.recipe()
        self.cleanup()

    @abstractmethod
    def prepare(self):
        pass
    @abstractmethod
    def recipe (self):
        pass
    @abstractmethod
    def cleanup (self):
        pass

class Recipe1(AbstractRecipe):
    def prepare(self):
        print('do the dishes')
        print('get raw materials')
    def recipe(self):
        print('execute the steps')
    def cleanup(self): pass
 
Recipe1().execute()
print("Recipe 1 execution completed")

class MicrowaveRecipe(AbstractRecipe):
    
    def prepare(self):
        print('do the dishes')
        print('get raw materials')
        print('switch on microwave')
    def recipe(self):
        print('execute the steps')
    def cleanup(self):
        print('switch off microwave')
    
MicrowaveRecipe().execute()
print("MicrowaveRecipe 1 execution completed")



#----------------------------------------------------------------



#----------------------------------------------------------------
#--------------Polymorphism Concept------------------------------
#----------------------------------------------------------------
class shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14159 * (self.radius**2)
    def perimeter(self):
        return 2 * 3.14159 * self.radius
    # Method to represent the Fan object as a string
    def __repr__(self):
        return repr(("Circle", self.radius ))


class square(shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side * self.side
    def perimeter(self):
        return 4 * self.side
    def __repr__(self):
        return repr(("Square with sides :", self.side ))

class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
    def __repr__(self):
        return repr(("Rectangle with sides :", self.length, "and", self.width ))

shapes = [circle(5), square(4), rectangle(2, 5)]

print('-------------------------------')
print(shapes[0])
print(shapes[1])
print(shapes[2])
print('-------------------------------')

for shape in shapes:
    print(f"The area of {shape} is {shape.area()} and the perimeter is :--  {shape.perimeter()}")

for shape in shapes:
    print(f"The area and perimeter of {shape} is {shape.area()} and {shape.perimeter()} respectively")

#--------------End of Prog---------------------------------------
#----------------------------------------------------------------
