print("hi")
print('hihihi'.upper())

msg1 = "PVSRAO"
msg2 = 'pvsrao'
print(msg2.upper())
print(msg1.lower())
print(msg2.capitalize())
#---------------------examples from the class
print("Hello World")  # Output: Hello World
print('Hello World')  # Output: Hello World


# FINDING THE TYPE OF A STRING
# The type() method allows you to find the type of a variable.
#     message = "Hello World"
#     print(type(message))  # Output: <class 'str'>

# STRING UTILITY METHODS
# The str class provides various methods to manipulate and inquire about strings.

# Converting to uppercase and lowercase
#     message = "hello"
#     print(message.upper())  # Output: HELLO
#     print(message.lower())  # Output: hello
#     print("hello".capitalize())  # Output: Hello
#     print('hello'.capitalize())  # Output: Hello

# Checking lower case, title case, and upper case
#     print('hello'.islower())  # Output: True
#     print('Hello'.islower())  # Output: False
#     print('Hello'.istitle())  # Output: True
#     print('hello'.istitle())  # Output: False
#     print('hello'.isupper())  # Output: False
#     print('Hello'.isupper())  # Output: False
#     print('HELLO'.isupper())  # Output: True

# Checking if a string is a numeric value
#     print('123'.isdigit())  # Output: True
#     print('A23'.isdigit())  # Output: False
#     print('2 3'.isdigit())  # Output: False
#     print('23'.isdigit())   # Output: True

# Checking if a string only contains alphabets or alphabets and numerals
#     print('23'.isalpha())   # Output: False
#     print('2A'.isalpha())   # Output: False
#     print('ABC'.isalpha())  # Output: True
#     print('ABC123'.isalnum())  # Output: True
#     print('ABC 123'.isalnum())  # Output: False

# Checking if a string ends or starts with a specific substring
#     print('Hello World'.endswith('World'))   # Output: True
#     print('Hello World'.endswith('ld'))      # Output: True
#     print('Hello World'.endswith('old'))     # Output: False
#     print('Hello World'.endswith('Wo'))      # Output: False
#     print('Hello World'.startswith('Wo'))    # Output: False
#     print('Hello World'.startswith('He'))    # Output: True
#     print('Hello World'.startswith('Hell0')) # Output: False
#     print('Hello World'.startswith('Hello')) # Output: True

# Finding a substring within a string
#     print('Hello World'.find('Hello'))   # Output: 0
#     print('Hello World'.find('ello'))    # Output: 1
#     print('Hello World'.find('Ello'))    # Output: -1
#     print('Hello World'.find('bello'))   # Output: -1
#     print('Hello World'.find('Ello'))    # Output: -1

# USING IN KEYWORD TO CHECK IN A STRING
# You can use the in keyword to check whether a character or sequence of characters exists within a specific set.
#     print('Hello' in 'Hello World')   # Output: True
#     print('ello' in 'Hello World')    # Output: True
#     print('Ello' in 'Hello World')    # Output: False
#     print('bello' in 'Hello World')   # Output: False

The String Module in Python
IMPORTING THE STRING MODULE AND EXPLORING CONSTANTS

    # import string
     
    # print(string.ascii_letters)        
    # # Output: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
     
    # print(string.ascii_lowercase)      
    # # Output: abcdefghijklmnopqrstuvwxyz
     
    # print(string.ascii_uppercase)      
    # # Output: ABCDEFGHIJKLMNOPQRSTUVWXYZ
     
    # print(string.digits)               
    # # Output: 0123456789
     
    # print(string.hexdigits)            
    # # Output: 0123456789abcdefABCDEF
     
    # print(string.punctuation)          
    # # Output: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
     
    # print(string.ascii_letters)        
    # # Output: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    
    # printing ascii value of a character  (a-z ==> 65 to 90    & A-Z ==> 97 to 112)
    # print(ord("A"))  # This prints the acii value of the character A
#---------------to print ascii vlaues-----------
import string

for ch in string.ascii_uppercase:
    print(ch,"   ", ord(ch))
#---------------To print Ascii value + determine vowel or not-----
import string
def isvowel(char):
    vs='aeiouAEIOU'
    return (char in vs)

for ch in string.ascii_lowercase:
    print(f"character is : {ch} Ascii Value is : {ord(ch)}  Vowel is : {isvowel(ch)}")
#---------------------------------
import string
for ch in string.ascii_lowercase:
    print(f"character is : {ch} Ascii Value is : {ord(ch)}  Vowel is : {ch in 'aeiouAEIOU'}")
#----------------------------------
#--------------------count uppercase in a given string
import string
def cucase(st):
    count=0
    print(st)
    for ch in st:
        if (ch in string.ascii_uppercase):
            count+=1
    return count
print(f"upper case count in AAA subbarao is {cucase('AAA')}")
#---------------------with While loop -count upppercase leters in a given string-----
import string
def cucase(str):
    ctr,i=0,0
    length =len(str)
    while i < len(str):
        if str[i] in string.ascii_uppercase:
            ctr+=1
        i+=1
    return ctr
print(cucase("AAA"))  
#--------------------------------------------------------------------
#-- find the num of consecutive identical chars in a given string --
# eg : HELLO  has 1 occurrance of LL

import string
def cid(text):
    cntr,i=0,1
    print("Given Text string is     :",text)
    # print(len(text))
    # for ch in text:
    #     print(ch)
    while i <(len(text)-1):
        if text[i+1]==text[i]:
            cntr+=1
        i+=1
    print("the count of consecutive identical chars is",cntr)
    

cid("bxaabb") # this is just a function call with the string paramter
cid("Hello Woorrlldd")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
# Instructions :
# Define a function named find_right_most_digit(text). The function takes one argument: text, which represents the string you want to search.
# Use a reversed for loop to iterate through the characters of text from right to left.
# Check if the character is a digit using the isdigit method. If it is, return the digit as an integer.
# If no digit is found, return -1.
#----------------this prog returns the number of digits in a given string value
ktr=0
def frmd(txt):
    l=len(txt)
    ctr=0
    print(txt,len(txt))
    for i in range(l-1,-1,-1):
        #print(i,txt[i])
        if(txt[i].isdigit()):
            ctr+=1
    return ctr

ktr=frmd ('K123456789P')
print("digit chars ",ktr)
#--------End of prog--------------------------------------------------
#----------------this prog returns the first integer from the given string as integer not as string or char 
#------i used a int() type casting
ktr=0
def frmd(txt):
    l=len(txt)
    print(txt,len(txt))
    for i in range(l-1,-1,-1):
        if(txt[i].isdigit()):
            return int(txt[i])
        
ktr=frmd ('K123456789xxx')
print("Right Most digit is ",ktr)

print("result is an integer",type(ktr))

#--------Part2 ; Same program with a function to reverse the txt-------------------------------
ktr=0
def frmd(txt):
    for ch in reversed(txt):
        if ch.isdigit():
            return int(ch)
    return -1

ktr=frmd ('K123456789asdfasdfasdfasdfasdfasdfasfsfxxx')
print("Right Most digit is ",ktr)
#--------End of prog------------------------------------
#----------------------------------------------------------
#Create a Python function named find_longest_word that identifies and returns the left-most longest word in a provided text.
# Utilize the split method for word extraction, and the len function to determine word length.
#  inout taken as string of words and tretuin the longest work in the sentence
# this is the bloody WORST WAY of doing it using the index of words etc
#--------------------WORST WAY OF CODING--------------------------
#--------------------WORST WAY OF CODING--------------------------
#--------------------WORST WAY OF CODING--------------------------
#--------------------WORST WAY OF CODING--------------------------
#--------------------WORST WAY OF CODING--------------------------
def lgword(txt):
    x=txt.split()
    wrdlen=len(x[0])
    flw=x[0]   #first word stored here
    print(x) 
    print ("words in the txt",len(x))
    #print ("first word length :",wrdlen)  #-- capuring the length of first word
    for i in range(1,len(x)-1,1):
        # print(x[i-1]," ",len(x[i-1])," ",x[i]," ",len(x[i]))
        if len(x[i])>wrdlen:
            wrdlen=len(x[i])
            flw=x[i]
            #print(flw)
    return flw

ktr=lgword('He is a mad fellow of aslfkasdf but xxxxxxsdlasdfasldfkjhaklsdf ssss dddddd dfdfd ds s s s s s s s s s d d d d f f f r r r r e e e e e w w w w w')
print(ktr)
#--------SMARTER WAY OF DOING------------------------------------
#--------SMARTER WAY OF DOING------------------------------------
#--------SMARTER WAY OF DOING------------------------------------
#--------SMARTER WAY OF DOING------------------------------------

def lgw(txt):
    if (txt==''):
        return -1
    wrdlen=0
    lngword=''

    for word in txt.split():
        if len(word)>wrdlen:
            lngword = word
            wrdlen = len(word)
    return lngword

wiput1='He is a mad fellow of aslfkasdf but xxxxxxsdlasdfasldfkjhaklsdf ssss dddddd dfdfd ds s s s s s s s s s d d d d f f f r r r r e e e e e w w w w w'
wiput2=''
wiput3='The quick brown fox jumps over the lazy dog'
ktr=lgw(wiput2)
print(ktr)

#--------End of prog------------------------------------
#----------------------------------------------------------
#--------check if 2 given words are anagrams or not----No need to import string lib--------------------------------
def is_anagram(t1,t2):
    print (sorted(t1.lower()), sorted(t2.lower()))

    if (sorted(t1.lower())==sorted(t2.lower())):
        return 'anagram'
    else:
        return 'not anagram'
    # if (sorted(t1)==sorted(t2)):
    #     return 'anagram'
    # else:
    #     return 'not anagram'
ktr=is_anagram('slient','LISTEN')
print(ktr)
#--------End of prog------------------------------------
#--------check if a given string is  hex or not-----------------------------------
def is_hex(t1):
    if t1=='':
        return False
    for ch in t1:
        if ch not in '0123456789abcdefABCDEF':
            return 'not hex'
    return 'HEX'
a1='ab6734FF'
a2='iuqwreiuwerqui'
ktr=is_hex(a2)
print(ktr)
#--------End of prog------------------------------------
#-------------------reverse a given word withoutusing the reversed function

def rword(t1):
    rw1=''
    rw2=''
    for ch in t1:
        rw1=ch+rw1
        rw2=rw2+ch
    print(t1)
    print(rw1)
    print(rw2)

a1='abcdefgh'
a2='0123456789'

rword(a2)
#--------End of prog------------------------------------



































































































































































