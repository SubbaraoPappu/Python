#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#-------------------------Advanced List handling----------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

numbers = ['zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']

# Print the entire list
print (numbers)
# Print the Length of list
print (len(numbers))
# print a specific element by index of the list
print (numbers[2])

# Print an element which is not in list by index
# Error : list index out of range
# print(numbers[100])

# To print part of the list with start and end positions given
# Pls note that end position is excluded
# here the 4th element is excluded and it prints list values from
# position 2,3 bt not 4
print(numbers[2:100])
print(numbers[:1212])
print(numbers[-12121:1212])

# You can omit the index while printing the lists

print(numbers[:6]) # print from start to 5yth element - 
#excludes inex 6 = this means it prints the first 6 elements of list


# print from 3 to end of list
print(numbers [3:]) 

# this prints the entire last as the index number are bot being specified and empty
print(numbers[:])


#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#Explore the STEP parameter with PRINTING List of values
# Syntax is print([start:end:step])
#---------------------------------------------------------------------------------------
#-*************************************************************************-

num1 = ['zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
print(num1[:])

# start to end with step of 2
# start with first element to end of list and skipping 2-1 elements of list
# this means it prints every alternative element of
print(num1[::2]) # ['zero', 'Two', 'Four', 'Six', 'Eight']

print(num1[2::2]) #['Two', 'Four', 'Six', 'Eight']

# prints 1,3,5 which are less than 6 and skips every alternate element from index 1 wihch is "One"
print(num1[1:6:2]) # prints 1,3,5 which are less than 6 and skips every alternate element from index 1 wihch is "One"

# REverse printing
print(num1[::-1]) # ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One', 'zero']
print(num1[:6:-1]) # ['Nine', 'Eight', 'Seven']


# Though looks absurd , starts ptinting the end element and then as sten is > length of the lsit , it will yield in only one value that is 'last element of the lsit'
print(num1[6:2:-1])  # ['Six', 'Five', 'Four', 'Three']

#Prints from end of list to start by skipping 1 element in between
print(num1[::-2]) # ['Nine', 'Seven', 'Five', 'Three', 'One']  

print(num1[::-3]) #['Nine', 'Six', 'Three', 'zero']

#--************************************************--
# ----------- Deleteing values from the list---------
#--************************************************--

print("#--************************************************--")
num2 = ['zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
print(num2[:])

del num2[3:] # deletes all elemetns from the list from index of 3 onwards
print(num2[:]) #Output :--> ['zero', 'One', 'Two']

print("#--************************************************--")
num2 = ['zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
print(num2[:])

# deletes values at inex positions 3,4 only excludes inex position 5
del num2[3:5] 
print(num2[:])

print("#--************************************************--")
num2 = ['zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
print(num2[:])

# deletes all values of the list , its as good as list with no values inside
del num2[:] 
print(num2[:])

num2=[0,1,2,3,4,5,6,7,8,9]
print(num2[:])

print("#--*******************REPLACE LIST VALUES *********************--")
num2 = ['zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
print(num2[:])
#now replace list values into the index positions 3 and 4
# sor that 'Three and Four" are replaced by '3 and 4".
num2[3:5]=[3,4]
print(num2[:])







#---------------------------------------------------------------------------------------
#------------------------Some more Puzzles--------------------------------------------
#---------------------------------------------------------------------------------------
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
print(numbers[3:8]) # ['Three', 'Four', 'Five', 'Six', 'Seven', 'Eight']
 
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
print(numbers[3:]) #['Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
 
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
print(numbers[::4]) #['Zero', 'Four', 'Eight']
 
# Please note that here in the above example
# end index element at 9 is ignored and 
# then the increment is 2 which means that from postion 2 onwards it adds 2 to the index
# which means that numbers at index 2,4,6,8 are selected 
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
print(numbers[2:9:2]) #['Two', 'Four','Six', 'Eight']
 
# stats with last element in the index and every alternate element in the reverse order
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
print(numbers[::-2])  # ['Nine', 'Seven', 'Five', 'Three', 'One']
# stats with last element in the index and every 2nd alternate element in the reverse order
print(numbers[::-3])  # ['Nine', 'Six', 'Three', 'Zero']

 
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
numbers[1:6] = [1, 2, 3, 4, 5]
print(numbers)  # ['Zero', 1, 2, 3, 4, 5, 'Six', 'Seven', 'Eight', 'Nine']
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#--------------------------------------------------------------------------
# ---------------Coding Exercise: Slice Alternate Elements-----------------
#--------------------------------------------------------------------------
# you are tasked with crafting a Python function, slice_alternate_elements, 
# designed to fetch all the even-indexed elements originating from a list of integers.
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------


# nlist = [10, 20, 30, 40, 50, 60]
# print(nlist) 
# print(nlist[0::2])

#print(slice_alternate_elements([10, 20, 30, 40, 50, 60]))  
# # Expected Output: [10, 30, 50]


def slice_alternate_elements(nlist):
    print("nlist is ::",nlist)
    if not nlist:
        print("null list")
        return nlist
    else:
        return nlist[0::2]
    
print(slice_alternate_elements([10, 20, 30, 40, 50, 60]))  
# # Expected Output: [10, 30, 50]
print(slice_alternate_elements([]))  
# # Expected Output: [10, 30, 50]

#---------------------------------------------------------------------------------------
#------------Coding Exercise: Reverse Each Chunk----------------
# create a Python function named reverse_chunks that reverses 
# every three elements in a given list of integers.
#---------------------------------------------------------------------------------------
def revchunks(nlist):
    if not nlist:
        print("null list")
        return nlist        
    else:
        for i in range(0, len(nlist),3):
            print ("i val ::--",i)
            print ('before ',nlist[i:i+3])
            nlist[i:i+3] = nlist[i:i+3][::-1]
            print ('after ',nlist[i:i+3])
        return nlist

print(revchunks([1, 2, 3, 4, 5, 6, 7, 8, 9]))  #[3, 2, 1, 6, 5, 4, 9, 8, 7]


#---------------------------------------------------------------------------------------
#------------Coding Exercise: Reorder and Eliminate Middle----------------
# create a Python function named reverse_chunks that reverses 
# every three elements in a given list of integers.
#---------------------------------------------------------------------------------------
def reorder_and_eliminate_middle(nlist):
    if not nlist:
        print("null list")
        return nlist 
    else:
        print("Given List ",nlist)
        slist = sorted(nlist, key=len, reverse=True)
        #print("sorted list is :=",slist)

        #print("lenth of list ",len(slist))
        #print ("ssss",((len(sorted(nlist, key=len, reverse=True))) % 2))

        if (len(slist)% 2) :
            #odd number of elements
            stpos = len(slist) // 2
            endpos = stpos+1
            #print ("stpos 1 - endpost",stpos, endpos)
            del slist[stpos:endpos]
            return slist
        else:
            stpos = (len(slist) // 2)-1
            endpos=stpos +2
            #print ("stpos 2 - endpost",stpos, endpos)
            del slist[stpos:endpos]
            return slist
    

print(reorder_and_eliminate_middle(["apple", "banana", "kiwi", "grapes", "mango"]))  
# # Output: ["banana", "grapes", "mango", "kiwi"]
print(reorder_and_eliminate_middle(["apple", "banana", "kiwi", "grapes"]))  
# Output: ["banana", "kiwi"]
 
print(reorder_and_eliminate_middle([]))  
# # Output: []
 
print(reorder_and_eliminate_middle(["apple"]))  
# # Output: []



#---------------------------------------------------------------------------------------
#--------------------------Coding Exercise: Reorder and Eliminate Middle----------------
#----------------- NOt so effective way of coding------------------------------------
def reorder_and_eliminate_middle(nlist):
    if not nlist:
        print("null list")
        return nlist 
    else:
        print("Given List ",nlist)
        slist = sorted(nlist, key=len, reverse=True)
        #print("sorted list is :=",slist)

        #print("lenth of list ",len(slist))
        #print ("ssss",((len(sorted(nlist, key=len, reverse=True))) % 2))

        if (len(slist)% 2) :
            #odd number of elements
            stpos = len(slist) // 2
            endpos = stpos+1
            #print ("stpos 1 - endpost",stpos, endpos)
            del slist[stpos:endpos]
            return slist
        else:
            stpos = (len(slist) // 2)-1
            endpos=stpos +2
            #print ("stpos 2 - endpost",stpos, endpos)
            del slist[stpos:endpos]
            return slist
    

print(reorder_and_eliminate_middle(["apple", "banana", "kiwi", "grapes", "mango"]))  
# # Output: ["banana", "grapes", "mango", "kiwi"]
print(reorder_and_eliminate_middle(["apple", "banana", "kiwi", "grapes"]))  
# Output: ["banana", "kiwi"]
 
print(reorder_and_eliminate_middle([]))  
# # Output: []
 
print(reorder_and_eliminate_middle(["apple"]))  
# # Output: []

#----------------- effective way of coding------------------------------------



#----------------------------------------------------------------------------------
# solution Logic : take the list and check for null list of elements and number of 
# elements <=2 then returns null list back to the cller
# othewise 
#   a) take the list as paramter
#   b) sort it and assign to slist
#   c) get the midpoint on the list with list length //2 
#   d) if len(list)%2 ==0 --> even number of elemeent then 
#   e)          delete from list with index values as midpoint -1 and mid point & return List
#   f) else if the list has odd number of elements
#   g)          delete the element at index point at midpoint  & return List
#----------------------------------------------------------------------------------

def reorder_and_eliminate_middle(nlist):
    if not nlist or len(nlist)<=2:
        print("null list")
        return []
    else:
        print("Given List ",nlist)
        slist = sorted(nlist, key=len, reverse=True)
        mpoint = len(slist)//2

        if (len(slist)%  2) == 0:
            del slist[mpoint-1:mpoint+1]
            #even  number of elements - we need to delete 2 items from list
            print ("stpos 1 - endpost",mpoint-1,mpoint+1)
            return slist
        else:
            #odd number of elements
            del slist[mpoint]
            return slist
    

print(reorder_and_eliminate_middle(["apple", "banana", "kiwi", "grapes", "mango"]))  
# # Output: ["banana", "grapes", "mango", "kiwi"]
print(reorder_and_eliminate_middle(["apple", "banana", "kiwi", "grapes"]))  
# Output: ["banana", "kiwi"]
 
print(reorder_and_eliminate_middle([]))  
# # Output: []
 
print(reorder_and_eliminate_middle(["apple"]))  
# # Output: []
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------


