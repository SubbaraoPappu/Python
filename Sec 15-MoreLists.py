#----------------------------------------------------------------------
# shtting exercise -- roataion of list of values for n times
#----------------------------------------------------------------------
def rotate_list(list, num):
    if not list:
        return "List empty"
    if num<=0:
        return "invalid rotate count"
    
    print(f"Given List is {list} and ration count is {num}")
    
    # for 4 lelments range runs from 0 to 3 but len function gives 4
    
    # Please note theat for loop variation
    # when you implement a simple for loop for x times you can use 
    #----------------------------------------------------------------------
    #   use  for i in range(x) 
    #                       instead of 
    #                               for i in range 0,x,1)
    #----------------------------------------------------------------------
    for k in range(num):
    #for k in range(0,num,1):  

        print(f"before round {k} the list is {list}")
        l_item = list[len(list)-1]
        for j in range (len(list)-1,-1,-1): # 0,1,2,3
            list[j]=list[j-1]
        list[0]=l_item
        print(f"After round {k} the list is {list}")

    print(f"\n\n\n\n\final list after {num} rotations is :::   {list}")
    
rotate_list(['subbu','pandu','baru','chellipapa'],4)
#--------------------------------END END-------------------------------
#--------------------------------END END-------------------------------
#--------------------------------END END-------------------------------
#--------------------------------END END-------------------------------

#----------------------------------------------------------------------
# Encoding a given list of workds with character shifting 
# wiht z or Z boundry conditions checks
#----------------------------------------------------------------------

def encode_strings(list):  
    enco_list=[]
    nl=list
    for k in nl:
        ew=''
        for ch in k:
            if ch !='z' and ch !='Z':
                ew=ew+chr(ord(ch)+1)
            elif ch=='z':
                ew=ew+'a'
            elif ch=='Z':
                ew=ew+'A'    


        #print(f"Old word is : {k} new word is : {ew}")
        enco_list.append(ew)
    return enco_list    

# function call test
# encode_strings(['abc', 'def'])

print(encode_strings(['zoo']))  # Output: ['app']
print(encode_strings(['aBA', 'def']))  # Output: ['bcd', 'efg']
print(encode_strings(['hello', 'WORLD']))  # Output: ['ifmmp', 'XPSME']
print(encode_strings(['']))  # Output: ['']
#--------------------------------END END-------------------------------
#--------------------------------END END-------------------------------
#--------------------------------END END-------------------------------



#----------------------------------------------------------------------
#------------------Alternate Merge of Two Lists------------------------
# In this exercise, you're tasked with merging two lists by alternating 
# elements from each list. If one list is longer than the other, t
# he excess elements should be added to the end of the merged list.
#----------------------------------------------------------------------

def alternate_merge(list1, list2):
    merged_list=[]
    # print(list1)
    # print(len(list1))
    # print(list2)
    # print(len(list2))

    for i in range(0, max(len(list1),len(list2)),1):
        if i < len(list1):
            #print(list1[i])
            merged_list.append(list1[i])
        if i < len(list2):
            #print(list2[i])
            merged_list.append(list2[i])

    return merged_list
    #------------------------------
    # need to see if we can work with a While loop as well
    #------------------------------

    # while i<= max(len(list1),len(list2)):

    #     merged_list.append(list1[i])
    #     merged_list.append(list2[i])
    #     i+=1
    #print(f"merged final list is    :{merged_list}")

print(alternate_merge(['a', 'b'], ['c', 'd', 'e']))  
# Output: ['a', 'c', 'b', 'd', 'e']
    
print(alternate_merge(['x', 'y', 'z'], ['1', '2']))  
# Output: ['x', '1', 'y', '2', 'z']
    
print(alternate_merge(['apple', 'banana'], ['grape', 'pineapple', 'blueberry']))  
# Output: ['apple', 'grape', 'banana', 'pineapple', 'blueberry']
    
print(alternate_merge([], ['a', 'b', 'c']))  
# Output: ['a', 'b', 'c']
    
print(alternate_merge(['short', 'words'], ['a_very_long_word', 'tiny']))  
# Output: ['short', 'a_very_long_word', 'words', 'tiny']

#--------------------------------END END-------------------------------
#--------------------------------END END-------------------------------
#--------------------------------END END-------------------------------

#----------------------------------------------------------------------
#----------------------------------------------------------------------
            Working with Lists of Custom Types
            Working with Lists of Custom Types
#----------------------------------------------------------------------
=========================
CREATING Country CLASS
======================
class Country:

    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def __repr__(self):
        return repr((self.name,self.population,self.area))
=========================
CREATING COUNTRY INSTANCES
==========================
Let's create instances of the Country class:

countries = [Country('India',1200,100),
                Country('China', 1400, 200),
                Country('USA', 120, 300)]

countries.append(Country('Russia',80,900))

We've created four instances representing different countries.

=================
SORTING COUNTRIES
==================
We can sort the list of countries based on certain attributes. Here, we're using the attrgetter function from the operator module:

# from operator import attrgetter
# countries.sort(key=attrgetter('population'), reverse=True)
# print(countries)

====================
FINDING Max AND Min
=====================
We can find the country with the maximum and minimum population or area:
    # print(max(countries, key=attrgetter('population')))
    # print(min(countries, key=attrgetter('population')))
    # print(min(countries, key=attrgetter('area')))
    # print(max(countries, key=attrgetter('area')))

#----------------------------------------------------------------------
#----------------------------------------------------------------------#----------------------------------------------------------------------
#----------------------------------------------------------------------
class Country:

    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def __repr__(self):
        return repr((self.name,self.population,self.area))

countries = [Country('India',1200,100),
                Country('China', 1400, 200),
                Country('USA', 120, 300)]

countries.append(Country('Russia',80,900))


# from operator import attrgetter
# countries.sort(key=attrgetter('population'), reverse=True)
# print(countries)

====================
FINDING Max AND Min
=====================
We can find the country with the maximum and minimum population or area:
    # print(max(countries, key=attrgetter('population')))
    # print(min(countries, key=attrgetter('population')))
    # print(min(countries, key=attrgetter('area')))
    # print(max(countries, key=attrgetter('area')))
#----------------------------------------------------------------------
#--------------------Anagram Checker with list -----------------------
# ----------------------------------------------------------------------
#----------------------------------------------------------------------
def is_anagram(string1, string2):
    print(string1, string2)
    if len(string1)!=len(string2):
        return False
    
    list1 = [0]*26
    list2 = [0]*26

    for char in string1:
        list1 [ ord(char)-ord('a')] += 1
    for char in string2:
        list2 [ ord(char)-ord('a')] += 1
    print(list1)
    print(list2)

    return(list1==list2)


print(is_anagram("listen", "silent"))  # Output: True
print(is_anagram("hello", "hey"))      # Output: False
print(is_anagram("apple", "ppale"))    # Output: True

#----------------------------------------------------------------------
#----------------------------------------------------------------------
#----------------------------------------------------------------------















