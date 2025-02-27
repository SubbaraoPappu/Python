i=5
if i>3:
    print(f"{i} is greater than 3")

i=2
if i>3:
    print(f"{i} is greater than 3")
elif i==3:
    print(f"{i} is equal to 3")
else:
    print(f"{i} is less than 3")  

#---triangle angles=180 example
def isvt(a1,a2,a3):
    if a1<=0 or a2<=0 or a3<=0:
        return False
    else:
        return a1+a2+a3==180
print(isvt(60,60,60)) # True
print(isvt(100,50,40)) # False  
print(isvt(190,-45,45)) # True 
#----------sum of divisors for a given number
def d1(a1):
    sum=0
    if a1 >0:
        print('pas1',a1)
        for i in range(1,a1+1):
            if(a1%i==0):
                sum=sum+i
                print(f"Divisor {i} sum {sum}")
    return sum
print(d1(122)) # 6+3+2+1=12
print(d1(100)) # 5+4+2+1=12

#----------------------------

#-----------------Example of perfect number ----------------
# A number is called perfect if the sum of its divisors is equal to the number itself.
# For example, 6 is a perfect number because 6=1+2+3    
# def isperfect(a1):
#     return d1(a1)==a1        
# print(isperfect(6)) # True
# print(isperfect(28)) # True
# print(isperfect(496)) # True


def d1(a1):
    sum=0
    if a1 >0:
        #print('pas1',a1)
        for i in range(1,a1):
            if(a1%i==0):
                sum=sum+i
                #print(f"Divisor {i} sum {sum}")
    return sum

def isperfect(a1):
    return d1(a1)==a1

for i in range (1,30000):
    if isperfect(i):
        print (f"The number {i} is perfect is {isperfect(i)}")
#----------------------------End ------------------------------
#-----------------print first 5 perfect numbers ----------------
# A number is called perfect if the sum of its divisors is equal to the number itself.
# For example, 6 is a perfect number because 6=1+2+3    
# def isperfect(a1):
#     return d1(a1)==a1        
# print(isperfect(6)) # True
# print(isperfect(28)) # True
# print(isperfect(496)) # True


def d1(a1):
    sum=0
    if a1 >0:
        #print('pas1',a1)
        for i in range(1,a1):
            if(a1%i==0):
                sum=sum+i
                #print(f"Divisor {i} sum {sum}")
    return sum

def isperfect(a1):
    return d1(a1)==a1

cntofnums=0

for i in range (1,3000000000):
        if cntofnums == 5:
            break
        else:
            if isperfect(i):
                cntofnums+=1
                print (f"The number {i} is perfect is {isperfect(i)}")
                
#----------------------------End ------------------------------

#-----------------find the last digit (units place) of a given number ----------------
def get_last_digit(n1):
    if (n1<=0):
        return False
    else:
        return n1%10

print (f"The last digit if 3453 is {get_last_digit(3453)}")
#----------------------------End ------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------
#---------------------------Now Logical Operators-------------------
#------------AND Operator----------------
print(True and True)         # output: True
print(True and False)        # output: False
print(False and True)        # output: False
print(False and False)       # output: False
#----------------OR Operator-----------------
print(True or False)         # output: True
print(False or True)         # output: True
print(True or True)          # output: True
print(False or False)        # output: False
#---------NOT Operator--------------
print(not True)              # output: False
print(not(True))             # output: False
print(not False)             # output: True
print(not(False))            # output: True
#-----------XOR ^  Operator---------------
print(True ^ True)           # output: False
print(True ^ False)          # output: True
print(False ^ True)          # output: True
print(False ^ False)         # output: False
#-----------------------------------------------
#------------- both numbers are even -- use AND operator
def botheven(i,j):
    if(i%2==0 and j%2==0):
        return True
    else:
        return False
    
print(f"both 4 and 6 are {botheven(4,6)}")
print(f"both 3 and 4 are {botheven(3,4)}")
#------------------anothe example for AND
def arebotheven(i,j):
    is_i_even = i%2==0
    is_j_even = j%2==0
    return is_i_even and is_j_even

print(f"both 2 and 4 are {arebotheven(2,4)}")
#------------- atleast one numbers are even -- use OR operator
def atleastoneeven(i,j):
    if(i%2==0 or j%2==0):
        return True
    else:
        return False
    
print(f"atlest one of 5 or 6 are even {atleastoneeven(5,6)}")
print(f"atlest one of 3 or 4 are even {atleastoneeven(3,4)}")
print(f"atlest one of 4 or 6 are even {atleastoneeven(4,6)}")
print(f"atlest one of 3 or 5 are even {atleastoneeven(3,5)}")
#-----------------Leap year example
def isitleap(year):
    if (year%4==00):
        return True
    else:
        return False
print(f"The year 2000 is a leap year : {isitleap(2000)}")
print(f"The year 2002 is a leap yead : {isitleap(2002)}")
#-----------------LEAP year Complex condition ffull checks ---------------------------
def isitleap(year):
    if year<=0:
        return False
    else:
        if not (year%4==00):
            return False
        else:
            if (year%4==0 and not year%100==0):
                return True
            elif (year%4==0 and  year%100==0):
                if(year%400==0):
                    return True
                else:
                    return False

print(f"The year 2048 is a leap year : {isitleap(2048)}")
print(f"The year 2000 is a leap year : {isitleap(2000)}")
print(f"The year 2400 is a leap year : {isitleap(2400)}")

print(f"The year 2100 is a leap year : {isitleap(2100)}")
print(f"The year 2200 is a leap year : {isitleap(2200)}")
print(f"The year 2300 is a leap year : {isitleap(2300)}")

print(f"The year 0 is a leap year : {isitleap(0)}")
#-------------------End of leap year prog----------------
#-----------------LEAP year Complex condition ffull checks ---------------------------
def isitleap(year):
    # validate year
    if year<=0:
        return False
    # not div 4 --> false
    if not year % 4 ==0 :
        return False
    # div by 4 and not div by 100 --> True
    if not year %100 ==0:
        return True
    # div by 4, div by 100 and div by 400 --> True
    if year %400 ==0 :
        return True
    return False

print(f"The year 2048 is a leap year : {isitleap(2048)}")
print(f"The year 2000 is a leap year : {isitleap(2000)}")
print(f"The year 2400 is a leap year : {isitleap(2400)}")

print(f"The year 2100 is a leap year : {isitleap(2100)}")
print(f"The year 2200 is a leap year : {isitleap(2200)}")
print(f"The year 2300 is a leap year : {isitleap(2300)}")

print(f"The year 0 is a leap year : {isitleap(0)}")
#-------------------End of leap year prog----------------

#--------------rt angle triangle with sides combination------
def isrtangtrg(s1,s2,s3):
    if (s1**2+s2**2==s3**2):
        return True
    elif (s1**2+s3**2==s2**2):
        return True
    elif (s2**2+s3**2==s1**2):
        return True
    else:
        return False
        
print(f"Sides 3,4,5 are rt traingle : {isrtangtrg(3,4,5)}")
print(f"Sides 3,5,4 are rt traingle : {isrtangtrg(3,5,4)}")
print(f"Sides 4,5,3 are rt traingle : {isrtangtrg(4,5,3)}")
print(f"Sides 3,4,6 are rt traingle : {isrtangtrg(3,4,6)}")
#---------------another way
def isrtangtrg(s1,s2,s3):
    if ((s1**2+s2**2==s3**2) or (s1**2+s3**2==s2**2) or (s2**2+s3**2==s1**2)):
    #if (s1**2+s2**2==s3**2) or (s1**2+s3**2==s2**2) or (s2**2+s3**2==s1**2): -- this will also works
        return True
    else:
        return False
        
print(f"Sides 3,4,5 are rt traingle : {isrtangtrg(3,4,5)}")
#---------------another way
def isrtangtrg(s1,s2,s3):
    return True  if (s1**2+s2**2==s3**2) or (s1**2+s3**2==s2**2) or (s2**2+s3**2==s1**2) else False

print(f"Sides 3,4,5 are rt traingle : {isrtangtrg(3,4,5)}")
#-----------------end of program-----------------
#------------chek for prime or not
def isprime(num):
    if num<2:
        return False
    else:
        for i in range(2,num-1):
            return False if num%i==0 else True

print(f"the number 37 is a prime number :- {isprime(7)}")
#--------------------sum of squeare upto a limit
def sosn(limit):
    sum=0
    num=1
    while (sum+num**2) < limit:
        sum+=num**2
        print("number is ", num,"sumis :",sum)
        num+=1
    return sum

print(f"sus uptp limit 500 is {sosn(500)}")
#--------------------get num of digits in a given number
def getnums(num):
    if num<0:
        return "Invlaid numer"
    elif num==0:
        return "1"
    cntnums=0
    while num >0:
        num//=10
        cntnums+=1
    return cntnums

print(f"count of digits in the number 0 is {getnums(0)}")
print(f"count of digits in the number 1 is {getnums(1)}")
print(f"count of digits in the number -12 is {getnums(-12)}")
print(f"count of digits in the number 123 is {getnums(123)}")
print(f"count of digits in the number 123456789000 is {getnums(123456789000)}")
#--------------------end of prog-----------------

#----------------break and continue -------------
i = 1
while i < 11:
    if i == 5:
        break
    print(i, end=' ')
    i += 1
print("done")


i = 1
while i < 11:
    if i % 2 == 0:
        i += 1
        continue
    print(i, end=' ')
    i += 1
print("done")
#--------------------------------
#-----------------next fib number after the given threshold number
def nfbn(th):
    a,b=0,1
    while True:
        sum=a+b
        if(sum>th):
            return sum
            break
        else:
            a,b=b,sum

print(f"nxt fb num greater than 3 is {nfbn(3)}")
#-----------------end of prog--------------------------------
# ----------------print the fist x fibonacci numbers-------
def nfbn(n):
    a,b=0,1
    count=2
    print(a,end=" ")
    print(b,end=" ")
    while True:
        sum=a+b
        count+=1
        print(sum,end=" ")
        if count < n:
            a,b=b,sum
            continue
        else:
            break

print(f"\nPrint the first 5 fib numbers {nfbn(5)}")
#---------------end of progra,---------------------
