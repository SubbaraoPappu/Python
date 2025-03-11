# -----------------> Exeption Handling <---------------
# 1) ZeroDivisionError
# 2) TypeError
# 3) AttributeError
# 4) IndentationError

# Errors and exceptions# are inevitable in any program. 
# They can arise due to faulty logic, but also because of 
# discrepancies between expected and actual environment 
# conditions, like missing directories or incorrect 
# configurations.

# EXPLORING ERROR EXAMPLES

#     ZeroDivisionError: This occurs when you try to divide a number by zero.
#         >>> 1/0
#         ZeroDivisionError: division by zero

#     TypeError: This arises when an operation is performed on an inappropriate data type.
#         >>> '2' + 2
#         TypeError: unsupported operand type(s) for +: 'int' and 'str'

#     NameError: This happens when you try to access an undefined variable.
#         >>> value
#         NameError: name 'value' is not defined

#     AttributeError: This occurs when you try to access a non-existent attribute of an object.
#         >>> values.non_existing
#         AttributeError: 'list' object has no attribute 'non_existing'

#     IndentationError: This occurs due to improper indentation
#         >>>     values = [1,'1']
#         IndentationError: unexpected indent



#  |  Method resolution order:
#  |      ZeroDivisionError
#  |      ArithmeticError
#  |      Exception
#  |      BaseException
#  |      object



import builtins
help(builtins.ArithmeticError)

#  |  Method resolution order:
#  |      ZeroDivisionError
#  |      ArithmeticError        |  Base class for arithmetic errors.
#  |      Exception              |  Common base class for all non-exit exceptions.
#  |      BaseException          |  Common base class for all exceptions
#  |      object


#***************************************************************
# UNDERSTANDING EXCEPTION HIERARCHY IN PYTHON
#***************************************************************

import builtins
 
# List all names in builtins module
builtin_names = dir(builtins)
 
# Print first 100 names as an example
print("First 200 built-in names:", builtin_names[:200])

erlist=builtin_names[:200]
print(len(erlist))

 
# Show help for one of the exceptions, e.g., ZeroDivisionError
help(builtins.ZeroDivisionError)

#***************************************************************
# Getting started with Try Except Blocks
#***************************************************************
try:
    i=0
    j=10/i
except:
    print("exception caught")
    j=99
print(j)

#***************************************************************
# Multiple except blocks to catch different types of exceptioons
#***************************************************************
try:
    i=0
    j=10/i
    val=[1,'2']  # Note that this list contains both string and integer values
    print(sum(val)) # Here the sun function fails as string and integer can not be added

except ZeroDivisionError:
    print("Zero Division error Occurred")
    j=88
except TypeError:
    print("Type error Occurred")
    j=99
print(f"Value of j ::-- {j}")
print('end of program')

#***************************************************************
# Exception handling Puzzles
#***************************************************************



try:
    sum([1, '1'])
except TypeError as error:
    print(error)

# Output :  unsupported operand type(s) for +: 'int' and 'str'


try:
    i=0
    j=10/1
    val=[1,'2'] # Note that this list contains both string and integer values
    print(sum(val)) # Here the sun function fails as string and integer can not be added

except ZeroDivisionError as error1:  # error1 a string to catch the text of the error
    print("Zero Division error Occurred")
    print(error1)
    j=8
except TypeError as error2:
    print("Type error Occurred")
    print(error2)
    j=99
else:  #---------Only else block should be used for all exeptions classes
    print("excepgggggggggggggg")
finally:
    print("finalfinalfinal")

print(f"Value of j ::-- {j}")
print('end of program')
#----------------------


try:
    i = 0  # Simulating input from user
    j = 10 / i
finally:
    print("Finally")  # This line will be executed
    
# This line will NOT be executed because an exception is raised and not caught
print("End")

#-----------------------------
class CurrentyMismatch(BaseException): #extend either BaseException Or Exception class -- dont user Object class here
    
    def __init__(self,message):
        super().__init__(message)
        print ("dddddddddd",message)
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency  # Currency type like "USD", "INR" etc.
        self.amount = amount  # Numerical amount
    
    def __add__(self, other):
        if self.currency != other.currency:
            try :
                raise CurrentyMismatch("Currencies Do Not Match")
            except CurrentyMismatch as e:
                print(e)
                print("hhhh")
        total_amount = self.amount + other.amount
        return Currency(self.currency, total_amount)

    def __repr__(self):
        return repr((self.currency, self.amount))

value1 = Currency("USD", 20)
value2 = Currency("INR", 30)
# This will raise an error because we haven't defined how to add two Currency objects.
print(value1 + value2)  

#--------------------------Ananlysis of copilot---------------------------------
# The provided code defines two classes, `CurrentyMismatch` and `Currency`, to handle 
# currency operations and custom exceptions in Python.

# The `CurrentyMismatch` class is a custom exception that inherits from Python's built-in 
# `Exception` class. It overrides the `__init__` method to accept a `message` parameter, 
# which it passes to the base class constructor using `super().__init__(message)`. 
# This ensures that the custom exception behaves like a standard Python exception, 
# storing the error message for later access. Additionally, it prints the message to the 
# console, which can be useful for immediate debugging purposes.

# The `Currency` class represents a currency with a specific type and amount. 
# The `__init__` method initializes the `currency` and `amount` attributes. 
# The `__add__` method is overridden to define the behavior for adding two `Currency` objects. 
# It first checks if the currency types of the two objects match. If they do not, 
# it raises a `CurrentyMismatch` exception with an appropriate message. The exception is c
# aught within the `try-except` block, and the error message is printed along with an 
# additional debug message "hhhh". If the currency types match, it adds the amounts and 
# returns a new `Currency` object with the same currency type and the total amount.

# The `__repr__` method is overridden to provide a string representation of the `Currency` 
# object, which includes the currency type and amount in a tuple format.

# In the example usage, two `Currency` objects, `value1` and `value2`, are created with 
# different currency types ("USD" and "INR"). When attempting to add these two objects 
# using the `+` operator, the `__add__` method raises a `CurrentyMismatch` exception 
# because the currency types do not match. The `print(value1 + value2)` statement will 
# trigger this exception, demonstrating the custom error handling in action. The error 
# message "Currencies Do Not Match" and the debug message "hhhh" will be printed to the 
# console.
#--------------------------------------------------------------------------------------`

class CurrenciesDoNotMatchError(Exception):
    def __init__(self, message):
        super().__init__(message) 


# Currency class from our previous lecture
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency  # Currency type like "USD", "INR" etc.
        self.amount = amount  # Numerical amount
 
    def __repr__(self):
        return repr((self.currency, self.amount))
 
    def __add__(self, other):
        if self.currency != other.currency:
            raise CurrenciesDoNotMatchError(self.currency + " " + other.currency)
        total_amount = self.amount + other.amount
        return Currency(self.currency, total_amount)
 
 
value1 = Currency("USD", 20)
value2 = Currency("INR", 30)
 
# This will raise an exception because the currencies don't match.
print(value1 + value2)  





































