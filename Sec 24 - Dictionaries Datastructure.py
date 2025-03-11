occurances = dict(a=5, b=6, c=8)
occ2= {'a': 5, 'b': 6, 'c': 8}
print(occurances)  # {'a': 5, 'b': 6, 'c': 8}
print(type(occurances))  # <class 'dict'>

print(occ2)  # {'a': 5, 'b': 6, 'c': 8}
print(type(occ2))  # <class 'dict'>

# Adding a new key value pair of d=15
occurances['d'] = 15  
print(occurances)  # {'a': 5, 'b': 6, 'c': 8, 'd': 15}

#Modify the value for key 'd'
occurances['d'] = 10
print(occurances)  # {'a': 5, 'b': 6, 'c': 8, 'd': 10}

#printing the value for a key from the dict when we know that key exists
print(occurances['d'])  # 10

# Accessing a non-existent key raises a KeyError.
# print(occurances['e'])  # Uncommenting this will raise KeyError: 'e'

# To avoid this, use the get() method, providing a default value if needed.
print(occurances.get('d'))  # 10
print(occurances.get('e'))  # None
print(occurances.get('e', 10))  # 10

print(occurances)  # {'a': 5, 'b': 6, 'c': 8, 'd': 15}

#EXPLORING DICTIONARY METHODS
print(occurances.keys())  # dict_keys(['a', 'b', 'c', 'd'])
print(occurances.values())  # dict_values([5, 6, 8, 10])
print(occurances.items())  # dict_items([('a', 5), ('b', 6), ('c', 8), ('d', 10)])

#ITERATING A DICTIONARY
#You can iterate through key-value pairs in a dictionary.
for (key, value) in occurances.items():
    print(f"{key} {value}")  # Expected output:
                                # a 5
                                # b 6
                                # c 8
                                # d 10

#DELETING FROM A DICTIONARY
#You can delete a specific key-value pair using the del keyword.

occurances['a'] = 0
del occurances['a'] # Deletes the pair from the dictionay where key ='a'
print(occurances)  # {'b': 6, 'c': 8, 'd': 10}

#----------------------------------------------------------------------
PUZZLES

#updating the Value for a Key
user_info = {'name': 'John', 'age': 30, 'city': 'New York'}
user_info['age'] = 31 # - Updates the value where the key is 'age"
print(user_info)

# add new KV pair
user_info['zipcode']= 'AL980'
print(user_info)

#Delete city KV pair
del user_info['city']
print(user_info)

#Update value for a key
user_info['name'] = 'Raju'
print(user_info)

# add new KV pair
user_info['city']= 'Hyderabad'
print(user_info)
#-------------------------------------------------

text = "hello"      # Simple text variable with a value assigned
char_count = {}     # empty dictionary variable
for char in text:   # looping char in text variable
    if char in char_count:  
        char_count[char] += 1  # if the character from the text is found on the char_count 
                               # dictionary then the value for that key gets incremented
    else:
        char_count[char] = 1  # if the character from the text is NOT found on the char_count 
                               # dictionary then add the new KV pair to dictionary
# finally print the dictionary variable
print(char_count)   # Outout -->    {'h': 1, 'e': 1, 'l': 2, 'o': 1}
#-------------------------------------------------


dict_1 = {'a': 1, 'b': 2, 'c': 3}
dict_2 = {'c': 3, 'd': 4, 'e': 5}
# To conduct any set operations like union , intesection or difference 
# we need to convert the DIct into Set using set() type casting
# The result would be a set not a dictionary vaiable
common_keys = set(dict_1.keys()) & set(dict_2.keys())
print(common_keys)
print(type(common_keys))

#---------------------------------------------------
#  Take 2 independent lists with same number of elements
# now merge both into a dictioary variable using the zip method where
# Here key comes from the 1st Lsit and Value comes from 2nd List
# thus a KV pair is made and added to the dictionary variable

keys = ['a', 'b', 'c']
values = [1, 2, 3]
result = {k: v for k, v in zip(keys, values)}
print(result)           # Output --> {'a': 1, 'b': 2, 'c': 3}
print(type(result))     # Output --> <class 'dict'>
#-----------------------------------------------

#-------------Dictionary of Dictionalries----------------
# Here a dictionary users is created with 2 dictionary sets as the values
# users is a dictionary where its made of 2 more dictionarys user1 and user2
# both user1 and user2 have their KV pairs
# ---> Pls note that both use1 and user2 dictionarys does not have common Keys

users = {
    'user1': {'name': 'John', 'age': 30},
    'user2': {'lstname': 'Jane', 'height': 25}
}
print(users['user1']['name'])
print(users['user2']['lstname'])

print(users['user2']['height'])
print(users['user1']['age'])
print(users['user2']['name'])         # O/p is KeyError as there is no key as 'name' in user2 dict.
#-----------------------------------------------

squares = {x: x**2 for x in range(1, 6)}
print(squares) # O/p --> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#-----------------------------------------------

students = {"Alice": {"Math", "English"}, "Bob": {"Math", "Science"}}
common_subjects = set.intersection(*students.values())
print(common_subjects)

#----------------Counting Character Occurrences--------------
def count_characters(str1):
    if not str1:
        print('empty')
        return {}
    char_count = {}
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

print(count_characters("banana"))
#-------------------------------------------------------------
#--------Counting Character Occurrences - Ranga way-----------
def count_characters(str1):
    char_count = {}
    if not str1:
        print('empty')
        return {}

    for char in str1:
        char_count[char] = char_count.get(char,0) + 1
        #print(char_count)        
    return char_count

print(count_characters("bananssssnnnna"))
#O/p ---> {'b': 1, 'a': 3, 'n': 6, 's': 4}
#-------------------------------------------------------------
#--------Coding Exercise: Counting Word Occurrences---------
# Smartway of coding -- Implemented the char count logic for words as well
def count_words(str1):
    word_count = {}
    for word in str1.split():
        word_count[word] = word_count.get(word,0) +1
    return word_count

print(count_words("Hello world! Hello everyone."))
print(count_words("This is an is an awesome occasion. This has never happened before.")) 

#-------------------------------------------------------------
def squares_map(num):
    map = {}
    return {i: i**2 for i in range(1, num+1)}

print(squares_map(10)) 


#-------------------------------------------------------------
# Coding Exercise: Find Common Subjects
students = {"Alice": {"Math", "English"}, "Bob": {"Math", "Science"}}
common_subjects = set.intersection(*students.values())
print(common_subjects)
#-------------------------------------------------------------
def common_subjects(grade1,grade2, grade3):
    if not grade1 or not grade2 or not grade3:
            return set()
    all_grades=[grade1, grade2, grade3]

    for grade in all_grades:
        for subjects in grade.values():
            if not subjects:
                return set()
    
    is_grade1 = set.intersection(*grade1.values())
    is_grade2 = set.intersection(*grade1.values())
    is_grade3 = set.intersection(*grade1.values())

    return is_grade1 & is_grade2 & is_grade3

grade1 = {"Alice": {"Math", "English"}, "Bob": {"Math", "Science"}}
grade2 = {"Charlie": {"Math", "History"}, "David": {"Math", "English"}}
grade3 = {"Eva": {"Math", "Music"}, "Frank": {"Math", "Science"}}
grade4 = {}
grade5 = {"Gina": {}, "Hank": {"Math","History"}}

print(common_subjects(grade1, grade2, grade3))  # Output: {"Math"}
print(common_subjects(grade1, grade2, grade4))  # Output: set()
print(common_subjects(grade1, grade2, grade3, grade5))  # Output: {"Math"}
#-------------------------------------------------------------
# Below given is CoPilot explanation for the code above.
#---------------------------------------------------------
The common_subjects function is designed to find common subjects among 
three different grades. It takes three dictionaries as input, each 
representing a grade with student names as keys and sets of subjects as values. 
The function first checks if any of the input dictionaries are empty. 
If any of them are empty, it returns an empty set, indicating no common subjects.

Next, the function iterates through each grade and checks if any student 
has an empty set of subjects. If it finds any student with no subjects, 
it returns an empty set. This ensures that only grades with valid subjects 
are considered for finding common subjects.

The function then calculates the intersection of subjects for each grade 
using the set.intersection method. However, there is a mistake in the code 
where the intersection is calculated three times using grade1.values() 
instead of using grade2.values() and grade3.values() for the second and 
third grades, respectively. The correct approach would be to calculate 
the intersection for each grade separately.

Finally, the function returns the intersection of the three sets of 
common subjects. The provided test cases demonstrate the function's 
intended behavior, but due to the mistake in the code, the output 
might not be as expected. The function should be corrected to properly 
calculate the intersections for each grade.
#-------------------------------------------------------------
#  CoPilot explanation complete
#---------------------------------------------------------




#-------------------------------------------------------------
# CoPilot - Modified code to take variable number of arguments in function-
#--CoPilot Code---------------------------------------------

To modify the common_subjects function to accept a variable number of 
grade dictionaries, you can use the *args syntax. This allows the 
function to accept any number of arguments. Here is the updated code:

def common_subjects(*grades):
    if not grades or any(not grade for grade in grades):
        return set()
    
    for grade in grades:
        for subjects in grade.values():
            if not subjects:
                return set()
    
    common_subjects_set = set.intersection(*[set.intersection(*grade.values()) for grade in grades])
    return common_subjects_set

grade1 = {"Alice": {"Math", "English"}, "Bob": {"Math", "Science"}}
grade2 = {"Charlie": {"Math", "History"}, "David": {"Math", "English"}}
grade3 = {"Eva": {"Math", "Music"}, "Frank": {"Math", "Science"}}
grade4 = {}
grade5 = {"Gina": {}, "Hank": {"Math","History"}}

print(common_subjects(grade1, grade2, grade3))  # Output: {"Math"}
print(common_subjects(grade1, grade2, grade4))  # Output: set()d
print(common_subjects(grade1, grade2, grade3, grade5))  # Output: set()


In this updated version, the common_subjects function now accepts a variable 
number of grade dictionaries. It first checks if any of the grades are 
empty and returns an empty set if so. Then, it iterates through each 
grade to ensure that no student has an empty set of subjects. Finally, 
it calculates the intersection of subjects across all grades and returns 
the common subjects.

#-------------------------------------------------------------

Pls refer to the Copilot created documentation on this specific example.


#-------------------------------------------------------------
