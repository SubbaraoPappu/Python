#----------------------------------------------------------------
#     Linear seach
#----------------------------------------------------------------

def linear_search(lst,target):
    for index, value in enumerate(lst):
        if value==target:
            return index
    return None

result = linear_search([11,234,23,43,56,86,78], 78)
print("Found at index :-", result)

result = linear_search(['banana','grapes','chiku','guvava','cherry','fig'],'Mango')
print("Found at index :-", result)
#----------------------------------------------------------------

#----------------------------------------------------------------
#     Binary Search - Iterative approach
# PS : the given list must nbe sorted , if not, then sort it first
#----------------------------------------------------------------

#----------------Prog 1 - from Ranga----------------
def binary_search(lst, target):
    low = 0
    high=len(lst)-1
    print(f" list length and high index are  {len(lst)} and {high}")
    print (lst)
    print (target)

    while low <= high:
        mid=(low+high)//2
        print (f" Low  Mid and High are :-- {low} {mid} {high}")
        print ("                          ",lst[low], lst[mid], lst[high])

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            print ("mid < target")
            low = mid+1
        else:
            print ("mid > target")
            high = mid-1
    return None

result = binary_search([1,2,3,4,5,6,7,8,9],4)
print("Found at index :-", result)
#---------------Results are ---------------------------------------
 list length and high index are  9 and 8
[1, 2, 3, 4, 5, 6, 7, 8, 9]
4
 Low  Mid and High are :-- 0 4 8
                           1 5 9
mid > target
 Low  Mid and High are :-- 0 1 3
                           1 2 4
mid < target
 Low  Mid and High are :-- 2 2 3
                           3 3 4
mid < target
 Low  Mid and High are :-- 3 3 3
                           4 4 4
Found at index :- 3

[Done] exited with code=0 in 0.046 seconds

#------------------------------------------------------
#------------------------------------------------------
#------------------------------------------------------
#----------------Prog 2 - from subba----------------
# - Major diff is Low=mid and high=mid statement instead of 
#-  ranga made Low= mid+1 and hgih=mid-1
def binary_search(lst, target):
    low = 0
    high=len(lst)-1
    print(f" list length and high index are  {len(lst)} and {high}")
    print (lst)
    print (target)

    while low <= high:
        mid=(low+high)//2
        print (f" Low  Mid and High are :-- {low} {mid} {high}")
        print ("                          ",lst[low], lst[mid], lst[high])

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            print ("mid < target")
            low = mid
        else:
            print ("mid > target")
            high = mid
    return None

result = binary_search([1,2,3,4,5,6,7,8,9],4)
print("Found at index :-", result)
#---------------Results are ---------------------------------------
 list length and high index are  9 and 8
[1, 2, 3, 4, 5, 6, 7, 8, 9]
4
 Low  Mid and High are :-- 0 4 8
                           1 5 9
mid > target
 Low  Mid and High are :-- 0 2 4
                           1 3 5
mid < target
 Low  Mid and High are :-- 2 3 4
                           3 4 5
Found at index :- 3

[Done] exited with code=0 in 0.058 seconds
#------------------------------------------------------

#------------------------------------------------------
# PS : please note the number of iterations in Ranga program is more than subbu program
#------------------------------------------------------

#------------Subba - Binary search program with much debug print statements
def binary_search(lst, target):
    low = 0
    high=len(lst)-1
    while low <= high:
        mid=(low+high)//2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid
        else:
            high = mid
    return None

result = binary_search([1,2,3,4,5,6,7,8,9],4)
print("Found at index :-", result)

#-**********************************************************
#-----------Binary search in RECURSIVE Approch---------
#-**********************************************************
def binary_search_recursive(lst, target, low=0, high=None):
    if high is None:
        high = len(lst)-1
        
    if low > high:
        return None
    
    mid = (low+high)//2
    #print(f" LOW, MID, High are : {low}  {mid}  {high}")
    #print ("                     ",lst[low], lst[mid], lst[high])
    if lst[mid] == target:
        return  mid
    elif lst[mid] < target:
        low = mid + 1  # we are moving right
        #low=mid
        return binary_search_recursive(lst, target, low, high)
    else:
        high = mid-1 # we are moving Lef
        #high=mid
        return binary_search_recursive(lst, target, low, high)
    



result = binary_search_recursive([10,20,30,40,50,60,70,80,90],10)
print("Found at index :-", result)

result = binary_search_recursive([10,20,30,40,50,60,70,80,90],40)
print("Found at index :-", result)

result = binary_search_recursive([10,20,30,40,50,60,70,80,90],50)
print("Found at index :-", result)

result = binary_search_recursive([10,20,30,40,50,60,70,80,90],900)
print("Found at index :-", result)
#-**********************************************************
#-**********************************************************
#-**********************************************************
