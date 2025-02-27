#simple function definition and function calling anther function
def prnt4():
    for i in range(1,3):
        print ('hello '+" subbarao4")
def prnt5():
    for i in range(1,5):
        print ('hello '+" subbarao5")
        prnt4()
prnt5()

#paramter passign example
def para(times):
    print("time ::",times)

para(2)

#function return value
def calc(p1,p2):
    return p1 +" "+ p2
res=calc("k","subba")
print (f"result is {res}")

def calc(p1,p2):
    return p1 * p2
res=calc(2,4)
print (f"result is {res}")

#------------------------
def kub(p1):
    return p1**3

res=kub(2)
print (f"result is {res}")
#---------------------
def kub(a,b,c,d):
    return a*b*c*d

res=kub(-2,-43,4,-5)
print (f"result is {res}")
#---------------------
def kavg(a,b,c,d,e):
    return (a+b+c+d+e)/5

#res=kavg(4562,-43,4,-5,8)
#print (f"result is {res}")

print("Averge of 5 numbers is ::",kavg(4562,-43,4,-5,8))
#---------------------
def calculate_third_angle(angle1, angle2):
    return (180 - angle1 - angle2)

angle3=calculate_third_angle(8, 54)

print(f" then third angle is {angle3}")
#---------------------
#-------------------------
#----------sum of squares of first N even numbers------ 2 code pieces given here belo
def sum_sq_enumb(n):
    even_number=0
    sum=0
    for i in range(0,n):
        even_number=even_number+2;
        sum+=even_number**2
        print(i, even_number,sum)
    return sum

#res=sum_sq_enumb(5)
#print(res)

print(f"sum of 4 enven numbers is {sum_sq_enumb(4)}")
#-------------------------
def sum_sq_enumb(n):
    even_number=0
    sum=0
    for i in range(2,n*2+1,2):
        print(i)
        sum+=i**2
    return sum
print(f"sum of 5 enven numbers is {sum_sq_enumb(5)}")
#-------------------------

#----------sum of squares of N odd numbers---------------
def sum_sq_oddnumb(n):
    even_number=0
    sum=0
    for i in range(1,n*2+1,2):
        print(i)
        sum+=i**2
    return sum
print(f"sum of 5 enven numbers is {sum_sq_oddnumb(5)}")
#----------------factorial example
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3)) 
#-----------------
def f12(n):
    if n == 0:
        return 1
    else:
        res=1
        for i in range(n,1,-1):
            res=res*i
        return res
    
print("factorial of 0 is ", f12(0)) 




















