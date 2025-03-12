numlist = [1,2,3,2,1]
print(f"numlist  :-- {numlist}")  # Output: numlist  :-- [1, 2, 3, 2, 1]

#--Create List from List and 
# the duplictes from the list and then set is created
numset=set(numlist)
print(f"numset  :-- {numset}")  # Output: numset  :-- {1, 2, 3}

#-- Add element to set
numset.add(0)
print(f"numset after addition 0 :-- {numset}")  # Output: {0, 1, 2, 3}

# try to add dupicate to set again
numset.add(0)
print(f"numset after addition 0 duplicate :-- {numset}")  # Output:{0, 1, 2, 3}

numset.remove(0)
print(f"numset after deletion of 0 :-- {numset}")  # Output: {1, 2, 3}

#check if a value is in set or not --  it returns boolean ansers True or False

print(1 in numset)  # Output: True
print(1 in numset)  # Output: False

# -- Aggregate functions usage
print(numset)
numset.add(0)
numset.add(4)
print(f"numset prepared for aggregate functions trial :-- {numset}")

print(f"min of set :-- {min(numset)}")  # function --> min(set)
print(f"max of set :-- {max(numset)}")  # function --> max(set)
print(f"sum of set :-- {sum(numset)}")  # function --> sum(set)
print(f"numset :-- {numset}")
print(f"Length of set :-- {len(numset)}")  # function --> len(set)

#===============Set Functions usage=================================================
#  UNION --> Operator "|" or use 'union' keyword
#  INTERSECTION --> Operator "&" 'intersection' keyword
#  DIFFERENCE  --> Operator "-"  --> Subtraction operator or 'difference' keyword
#===================================================================================

seta={1,2,3,4,5}
setb={4,5,6,7,8,9,10}
print(f"seta :- {seta}  setb  :- {setb}")

print(f"union result using operator | :--> {seta | setb}")              #output --> 
result=seta.union(setb)
print(f"using union keyword :-->  {result}")

print(f"Intersection result using operator & :--> {seta & setb}")       #output --> 
result=seta.intersection(setb)
print (f"using intersection keyword :--> {result}")


print(f" using difference operator -- seta - setb :-- {seta - setb}")
result=seta.difference(setb)
print(f" using difference keyword -- seta.difference(setb) :-- {result}")

print(f" using difference operator -- setb - seta  :-- {setb - seta}")
result=setb.difference(seta)
print(f" using difference keyword -- setb.difference(seta) :-- {result}")

#===============Set Functions Unpacking Lists and Sets=======================
# Unpacking Lists and Sets
# In Python, you can use the * operator to unpack elements 
# from a list or a set and pass them as arguments to a function. 
#=========================================================================

def print_values(num1, num2, num3):
    print(num1)
    print(num2)
    print(num3)
 
numbers = [10, 20, 30]
print_values(*numbers)

scores = {85, 90, 75}
print(scores)
print_values(*scores)


scores = {85, 90, 75}
print(scores)

numset={645,345,567,912,109,212,90}
print(numset)   

numset2={85,90,754545}
print(numset2)   
#------------------------------------------------------------------------------------------------------
# The order of elements in the set numset2 when printed as {90, 75, 85} is due to the unordered nature 
# of sets in Python. Sets are implemented using hash tables, and the order of elements is determined 
# by their hash values, not by the order in which they were added.

# Explanation:
# Unordered Nature of Sets: Sets in Python are inherently unordered collections. This means that the 
# elements in a set do not have a specific order, and their arrangement can change. The primary 
# purpose of a set is to provide fast membership testing and to ensure that all elements are unique.

# Internal Implementation: The internal implementation of sets in Python uses a hash table. When 
# elements are added to a set, they are hashed and placed into the hash table. The order in which 
# elements are stored in the hash table is determined by their hash values, not by the order in 
# which they were added.

# Printing Sets: When you print a set, Python iterates over the elements in the hash table and 
# displays them. The order of elements in the output may differ from the order in which they 
# were added due to the unordered nature of sets. The specific order in which elements are printed 
# can vary between different runs of the program or different versions of Python.

# Example Output:
# In the example provided, the set numset2 might be printed as {90, 75, 85}. This variation 
# in order is a result of the internal organization of the set and the way elements are hashed 
# and stored. The order is not guaranteed to be consistent and can change.

# Conclusion:
# The fact that numset2 appears in the order {90, 75, 85} when printed is due to the unordered 
# nature of sets in Python. Sets are designed to provide unique elements and fast membership 
# testing, not to maintain any specific order. If you need an ordered collection, you should 
# use a list or another ordered data structure. The order of elements in a set should not be 
# relied upon, as it can vary.
   
#------------------------------------------------------------------------------------------------------
# creating a set by passing list to the set keyword/function with duplicates
# the duplicates are removed and s1 set is created with unique values
s1=set([1,2,3,4,5,4,3,5])
print (s1)      # Output --> {1, 2, 3, 4, 5}

#-- Creating a list from the set
s1={1,2,3,4,5,6,7}
slist=list(s1)
print(slist)        #Output --> [1, 2, 3, 4, 5, 6, 7]

#------------------------------------------------------------------------------------------------------
# ==========================list of sets============================

# the above is a list containing 3 sets set([1,2,3]), set([3,4,5]) & set([5,6,7])
listofsets=[set([1,2,3]), set([3,4,5]), set([5,6,7])]
# - WE are unpacking the values (which are sets actually) from the List with *operator
# and passig them to set.union method as individual values 
# then it removes the duplicates and created the new set
newset=set.union(*listofsets)
print(f"The list values are (which are sets) :-->{listofsets}")
print(f"newset is created from above lsit with set.union operator :--> {newset}")

#-----------------------------------some more Lists with sets and union on them----------------------
list_of_sets_1 = [set([1, 2]), set([3, 4]), set([5, 6])]
list_of_sets_2 = [set([5, 6]), set([7, 8])]

print("\ndirect print for list_of_sets_1           ",list_of_sets_1)
print("print unpacked elements for list_of_sets_1   ",*list_of_sets_1)
print("\ndirect print for list_of_sets_1           ",list_of_sets_2)
print("print unpacked elements for list_of_sets_1  ",*list_of_sets_2)

union_result = set.union(*list_of_sets_1, *list_of_sets_2)
print(f"new set by unpacking list 1 and 2 with set.union method (no dups), Restuls :-- >>>   {union_result}")

#----------------create 2 sets individually and union on them--------------
ulist1=set.union(*list_of_sets_1) #Unpack the list and pas to st.union method
print(f"Unpacked List of set 1 (unpacked and dup removed) ulist1:-->  {ulist1}")

ulist2=set.union(*list_of_sets_2) #Unpack the list and pas to st.union method
print(f"Unpacked List of set 2 (unpacked and dup removed) ulist2:-->  {ulist2}")


newset = ulist1.union(ulist2)
print(f"\nnew set by set.unon on ulis1 and ulist2, Result  :-- >> {newset}")

#-----------------------Comprehension on sets----------------------------------------------

#--------------------Sets creation with Comprehension---------------------------------------------------------------------
numlist1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
set1 = {x for x in numlist1 if x % 2 == 0}
print(set1)         #  Op : {2, 4, 6, 8, 10}

result = {x**2 for x in numlist1 if x % 2 == 0}
print(result)       #   Op : {64, 100, 4, 36, 16}

num = 5
result = {x for x in range(num, 101, num)}
print(result)
# Output --> {5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100}


#--------------------List creation with Comprehension---------------------------------------------------------------------
numlist1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newlist = [x for x in numlist1 if x % 2 == 0]
print(newlist)      #  Op : [2, 4, 6, 8, 10]

newlist2 = [x**2 for x in numlist1 if x % 2 == 0]
print(newlist2)      #  Op : [4, 16, 36, 64, 100]

num = 5
result = [x for x in range(num, 101, num)]
print(result)
# Output -->  [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
#-----------------------------------------------------------------------------------------
my_list = [1, 2, 3, 2, 1, 4, 5, 3]
result = set(my_list)
print(result)
    
string_1 = "hello"
string_2 = "world"
    
result = set(string_1) | set(string_2)
print(result)
    
list_of_sets = [{1, 2, 3}, {3, 4, 5}, {5, 6, 7}]
result = set.intersection(*list_of_sets)
print(result)
#------------------------------------------------------------------------------------------------------

WHAT DID WE LEARN?
    Union operation (s1.union(s2) or s1 | s2) combines elements from two sets.
    Difference operation (s1.difference(s2) or s1 - s2) removes common elements from the first set.
    Set comprehension ({x**2 for x in numbers if x % 2 == 0}) creates a set of squared numbers for even elements.
    Using set() efficiently removes duplicates from a list, as sets only store unique elements.
    Combining unique characters from strings with set(string_1) | set(string_2).
    Finding common elements in a list of sets with set.intersection(*list_of_sets).


#------------------------------------------------------------------------------------------------------
#  Find Intersection Between Multiples of Two Numbers
#------------------------------------------------------------------------------------------------------
def find_intersection(num1, num2, limit):
    print(f"num1, num2, limt  :--> {num1, num2, limit}")

    if num1<=0 or num2 <=0:
        return set()

    num1set={x for x in range(num1, limit+1,num1)}
    print("num1set",num1set)
    num2set={x for x in range(num2, limit+1,num2)}
    print("num1set",num2set)
    result=num1set.intersection(num2set)
    return result

print(find_intersection(4,16,24))

#------------------------------------------------------------------------------------------------------
def unique_colors(p1, p2):
    if not p1 and not p2:
        return set()
   
    return (p1.union(p2) - p1.intersection(p2))
 

# # Examples
print(unique_colors({"red", "blue"}, {"blue", "green"}))         
# # Output: {"red", "green"}
    
print(unique_colors({"purple", "yellow"}, {"yellow", "pink"}))   
# # Output: {"purple", "pink"}
    
print(unique_colors({"orange", "cyan"}, {"cyan", "magenta"}))    
# # Output: {"orange", "magenta"}



#---------------------Shop List merge---------------------------------------------------------------------------------
#-----------My PRogam -- Crude and inefficient-------------------------------------------------------------------------------

def merge_shopping_lists(*shoplists):
    #print("infun")
    lstfinal = set()
    #print("listfinal",lstfinal)
    #print(type(lstfinal))
    for lst in shoplists:
        #print("ssss")
        #print("lst is :::",lst)
        lstfinal=lstfinal | lst
    #print(lstfinal)
    return lstfinal

list1 = {"apples", "bananas", "cherries"}
list2 = {"bananas", "dates", "eggs"}
list3 = {"cherries", "dates", "figs"}

print(merge_shopping_lists(list1, list2, list3))
# Output: {"apples", "bananas", "cherries", "dates", "eggs", "figs"}
 
list4 = {"bread", "milk"}
list5 = {"milk", "eggs", "juice"}
print(merge_shopping_lists(list4, list5))
# Output: {"bread", "milk", "eggs", "juice"}

#--------------Ranga Program -----------------------------------------------------
# --------it used "set.union() to unitie all the elements of the list
# Hence we passed the unpacked elements list as a arguments 
# Eg :  set.union(*lists)  this retuns a set 
# --------------------------------------------------------------------------------
def merge_shopping_lists(*lists):
    if not lists:
        return set()
    return set.union(*lists)

list1 = {"apples", "bananas", "cherries"}
list2 = {"bananas", "dates", "eggs"}
list3 = {"cherries", "dates", "figs"}

print(merge_shopping_lists(list1, list2, list3))
# Output: {"apples", "bananas", "cherries", "dates", "eggs", "figs"}
 
list4 = {"bread", "milk"}
list5 = {"milk", "eggs", "juice"}
print(merge_shopping_lists(list4, list5))
# Output: {"bread", "milk", "eggs", "juice"}

#------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------

































s1=[1,2,3,4]
print("s1 list",s1)

s1={1,2,3,4}
print("s1 set",s1)



setb=set()              # Empty set definition
setc={}                 # empty Dict definition
print(type(setb))               <class 'set'>
print(type(setc))               <class 'dict'>


# def greet(*names):
#     """Greet multiple people."""
#     for name in names:
#         print(f"Hello, {name}!")

# # Calling the function with a variable number of arguments
# greet("Alice", "Bob", "Charlie")


# def mixed_function(*args, **kwargs):
#     """Handle both positional and keyword arguments."""
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)

# # Calling the function with both positional and keyword arguments
# mixed_function(1, 2, 3, name="Alice", age=30)
