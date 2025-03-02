#---------Intro to DS----------
marks=[78,57,50,90]
print(marks)
marks.append(20) # to add a new value to the list at the end of the list
print(marks)

marks.insert(2,999) # to insert a new value in the location 3
print(marks)
marks.insert(5,444) # to insert a new value in the location 6
print(marks)
marks.remove(999) #--To remove marks 99999 from the list
print(marks)
marks.remove(444) #To remove a specific value from the list -- can be used if only if you know the list of marks
print(marks)
print(90 in marks) #--Check if the list contains the marks 90 or not
print(len(marks))
print(marks[4]) #marks in index location 5
print(marks.index(57)) # get the index location for marks57
print('---------')

print(marks.index(58)) # get the index location for marks58, as there is not 58 value in the list -- it will return an error

# print(sum(marks))
# print(sum(marks)/len(marks))
# print(max(marks))
# print(min(marks))

#----------------------------------------------------
#-----------create a function to accept a lsit of values and a number
# then chek if the list contains at least 1 value < number
def has_greater_element(numbers,value):
    if(len(numbers))<=0:
        return False
    else:
        if max(numbers)>value:
            return True
        else:
            return False
            
print(has_greater_element([30,35,39,45],99))

print(has_greater_element([10, 20, 30], 15))      # Output: True
print(has_greater_element([5, 7, 8], 10))        # Output: False
print(has_greater_element([], 5))                 # Output: False
#-----------------------SMART WAY belo------------------
def has_greater_element(numbers,value):
    if not numbers:
        return False
    for num in numbers:
        if num > value:
            return True
    return False
    
print(has_greater_element([30,35,39,45],99))

print(has_greater_element([10, 20, 30], 15))      # Output: True
print(has_greater_element([5, 7, 8], 10))        # Output: False
print(has_greater_element([], 5))                 # Output: False
#------------------------------------------------------------
#-----------------Char and String Lists
animals = ['Cat', 'Dog', 'Elephant']
print(animals)  # Output: ['Cat', 'Dog', 'Elephant']
print(len(animals))     # Output: 3
# print(animals[2])   # Output: Elephant
# print(animals[1])   # Output: Dog
# print(animals[0])   # Output: Cat
#You can use the del statement to remove an element from a list by its index.

del animals[2] # Elephant Removed
print(animals)      #Output:['Cat', 'Dog']

animals.extend(['Giraffe', 'Horse'])  # Output: ['Cat', 'Dog', 'Giraffe', 'Horse']
print(animals)

animals += ['Lion', 'Monkey']
print(animals)  # Output: ['Cat', 'Dog', 'Giraffe', 'Horse', 'Lion', 'Monkey']

#You can add a single element to a list using the append() method.
animals.append(10)
print(animals)      # Output: ['Cat', 'Dog', 'Giraffe', 'Horse', 'Lion', 'Monkey', 10]
#--------NegativeIndexing---------------------
print(animals[-1]) #Prints the last element of the list
print(animals[-3]) #prints teh 3rd element from the last of the list

numbers = [4, 2, 9, 1]
print(numbers)

numbers.sort()
print (numbers)

numbers.reverse()
print(numbers)
#--------------------example -1-----------------
#determine if the sum of the elements in two given lists is equal, without resorting to built-in functions (like sum). 
#---------------Smart Prog---------------------
def are_sums_equal(list1, list2):
    if not list1 or not list2:
        return False
    if sum(list1)==sum(list2):
        return True
    else:
        return False
print(are_sums_equal([10, 20, 30], [15, 25, 21]))  # Output: True
print(are_sums_equal([5, 10, 15], [5, 10, 14]))  # Output: False
print(are_sums_equal([1, 2, 3, 4], [4, 3, 2, 1]))  # Output: True
print(are_sums_equal([], [4, 3, -7]))  # Output: False
print(are_sums_equal([1, 2], []))  # Output: False
#-------------------------Stuppid Program------------------------------
def are_sums_equal(list1, list2):
    sum1,sum2=0,0
    if not list1 or not list2:
        return False
    for l1 in list1:
        sum1+=l1
    for l2 in list2:
        sum2+=l2
    if sum1==sum2:
        return True
    else:
        return False

print(are_sums_equal([10, 20, 30], [15, 25, 20]))  # Output: True

print(are_sums_equal([5, 10, 15], [5, 10, 14]))  # Output: False
print(are_sums_equal([1, 2, 3, 4], [4, 3, 2, 1]))  # Output: True
print(are_sums_equal([], [4, 3, -7]))  # Output: False
print(are_sums_equal([1, 2], []))  # Output: False
#--------------------------------------------------------
#Sorting, Looping, and Reversing Lists
#--------------------------------------------------------
REVERSING A LIST
In-Place Reversal: Using the reverse() method, you can reverse a list in-place. This action directly modifies the original list.
#--------------------------------------------------------
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
numbers.reverse()
print(numbers)  # ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One', 'Zero']
#--------------------------------------------------------
Looping Through a List in Reverse: The reversed() function allows you to access elements in reverse order without changing the original list.
for number in reversed(numbers):
    print(number)
# This prints the elements in reverse order.
#--------------------------------------------------------
SORTING A LIST
#--------------------------------------------------------
In-Place Sorting: The sort() method provides in-place sorting of the list, thereby altering the original list.
#--------------------------------------------------------
numbers.sort()
print(numbers)  # ['Eight', 'Five', 'Four', 'Nine', 'One', 'Seven', 'Six', 'Three', 'Two', 'Zero']
#--------------------------------------------------------
Accessing Elements in Sorted Order: To gain access to elements in a sorted order without affecting the original list, use the sorted() function.
#--------------------------------------------------------
for number in sorted(numbers):
    print(number)
# This prints the elements in sorted order.

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
# numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
# print(numbers)
# numbers.reverse()
# print(numbers)  # ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One', 'Zero']

# numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
# for n in reversed(numbers):
#     print(n)  #

#---------------inplace-Sorting
# numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
# print(numbers)
# numbers.sort()
# print(numbers)


#--Accessgin the sorted list without alteing the original
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
# print(numbers)
# for n in sorted(numbers):
#     print(n)
# print(numbers)


#-Sorting with criteria like lenth and reversing order etc etc
#- Ascendig order of lenth
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
for n in sorted(numbers,key=len):
    print(n)
# -- Sorting in desc order of lenth
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
for n in sorted(numbers,key=len, reverse=True):
    print(n)

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#==============Deep Dig here when you have 3 lette list only then reverse=true has no effect
numbers = ['One', 'Two', 'Six']
for n in sorted(numbers,key=len,reverse=True):
    print(n)
for n in sorted(numbers,key=len):
    print(n)

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
def is_list_sorted(list):
    if not list:
        return True
    list1=list
    list2=sorted(list)
    
    #print(list)
    #print (sorted(list))
    for i in range(0,len(list)):
        if list1[i]!=list2[i]:
            return False
    return True
            
print(is_list_sorted([10, 20, 30]))   # Output: True
print(is_list_sorted([10, 30, 20]))   # Output: False
print(is_list_sorted([30, 20, 10]))   # Output: False
print(is_list_sorted([]))             # Output: True
#------------------------------------------------------------------------------------------------
#----------------------------------Sorting without 2 lists----------------------------------------
#-----------------Just oprate on the given list and iterate between the elements with index-------
def is_list_sorted(list):
    if not list:
        return True
    #print(list, len(list))
    for i in range(0,len(list)-1):
        if list[i]> list[i+1]:
            return False
    return True
            
print(is_list_sorted([10,20,30,40,50,60,70,90,80]))   # Output: False
print(is_list_sorted([10, 30, 20]))   # Output: False
print(is_list_sorted([30, 20, 10]))   # Output: False
print(is_list_sorted([10,20,30,40]))   # Output: True
print(is_list_sorted([]))             # Output: True


#------------------------------------------------------------------------------------------------
#------------------------Revering a list wihtout functions only using while loops------------------
def reverse_list(list):
        start=0
        end=len(list)-1
        print(list)
        while(start<end):
            #print(f"Start :{start} end: {end}")
            list[start],list[end]=list[end],list[start]
            start+=1
            end-=1
            #print(list)
        return list
print(reverse_list([10,20,30,40,50,60]))      # Output: [30, 20, 10]
print(reverse_list([10, 20, 30]))      # Output: [30, 20, 10]
print(reverse_list([5, 15, 25, 35]))   # Output: [35, 25, 15, 5]
print(reverse_list([1]))               # Output: [1]
#------------------------------------------------------------------------------------------------
#---------------------------------Finding factors of a given number as list-----------------------
def find_factors(number):
    factors=[]
    if number<=0:
        return False
    for i in range(1,number+1,1):
        if number%i == 0:
            factors.append(i)
    return factors        


print(find_factors(12))  # Output: [1, 2, 3, 4, 6, 12]
print(find_factors(15))  # Output: [1, 3, 5, 15]
print(find_factors(7))   # Output: [1, 7]
print(find_factors(0))   # Output: False
#------------------------------------------------------------------------------------------------
#-----Finding multiples for a given number as list wihch are less than the given upper limt------   
#------------------------------with for loops and no while loop used---------------------------
def find_multiples(num, limit):
    multiples=[]
    lim=0
    if num<=0 or limit<=0:
        return False
    if num>limit:
        return multiples
    if limit%num>0:
        lim=(limit//num)+1
    elif limit%num==0:
        lim=(limit//num)
    #print lim
    for i in range(1,lim):
        multiples.append(num*i)
    return multiples

print (find_multiples(2, 12))
print (find_multiples(3, 12))
print (find_multiples(5, 50))
print (find_multiples(50, 50))
print (find_multiples(90, 50))
#----------------------------------while loop used------------------------------------------
def find_multiples(num, limit):
    multiples=[]
    if num<=0 or limit<=0:
        return False
    multiple=num
    while multiple<limit:
        multiples.append(multiple)
        multiple+=num
    return multiples

print (find_multiples(2, 12))
print (find_multiples(3, 12))
print (find_multiples(5, 50))
print (find_multiples(50, 50))
print (find_multiples(90, 50))
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------





