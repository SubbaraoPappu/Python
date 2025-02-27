print(type(5))
print(type(5.0))
print(type('5'))
print(type(True))   

value1 = 4.5
value2 = 3.2
print(value1 + value2)  # Output: 7.7
print(value1 - value2)  # Output: 1.2999999999999998
print(value1 / value2)  # Output: 1.40625
print(value1 % value2)  # Output: 1.2999999999999998


def csi(principal, interest, duration):
    total = principal + (principal * interest * 0.01 * duration)
    return total

print(csi(10000, 5, 5))  # Output: 12500.0

#----------------------------
i = 1
i = i + 1
print(i)  # Output: 2

i += 1
print(i)  # Output: 3  

i += 1
print(i)  # Output: 4
    
i -= 1
print(i)  # Output: 3
    
i /= 1
print(i)  # Output: 3.0
    
i *= 2
print(i)  # Output: 6.0
#------------------------Decimal class import examples
import decimal 
from decimal import Decimal

value1=Decimal('4.5')
value2=Decimal('3.2')
res=value1-value2
print(res)  # Output: 1.3   

v1=4.5  #flota variable
v2=3.2
res=v1-v2
print(res)  # Output: 1.3 
#------------------importng math class
import math

print(math.pi)       # Outputs: 3.141592653589793
print(math.e)        # Outputs: 2.718281828459045
#------------------------Boolean data type

print(True)  # Output: True
print(False)  # Output: False

i = 10
print(i >= 15)  # Output: False
print(i >= 10)  # Output: True
print(i > 10)  # Output: False
print(i <= 10)  # Output: True
print(i < 10)  # Output: False
print(i == 10)  # Output: True
print(i == 11)  # Output: False
#----------------------boolean

num_int = 7
num_float = float(num_int)
print(num_float)
 
num_float = 3.14
num_int = int(num_float)
print(num_int)
 
is_raining = True
int_value = int(is_raining)
print(int_value)
 
str_num = "123"
num = int(str_num)
print(num)
 
str_num = "3.14"
num = float(str_num)
print(num)
 
num = 10
str_num = str(num)
print(str_num)
 
is_true = True
str_bool = str(is_true)
print(str_bool)
 
print(bool('True'))
print(bool('true'))
print(bool('false'))
print(bool(''))
#------------
def k(speed):
    return speed==200
    
print(k(2199))
