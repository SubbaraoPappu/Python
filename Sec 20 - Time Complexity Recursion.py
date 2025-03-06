# CONSTANT TIME COMPLEXITY - O(1)

def get_first_element(arr):
    return arr[0]
 
# Try it out
print(get_first_element([1, 2, 3]))  # Output: 1


# LINEAR TIME COMPLEXITY - O(n)

def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val
print(find_max([1, 2, 3]))  # Output: 3 



# QUADRATIC TIME COMPLEXITY - O(n^2)

def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)
 
# Try it out
print_pairs([1, 2, 3])

# O(1) means the time to complete is constant and does not depend on the input size.
# O(n) means the time to complete grows linearly as the input size grows.
# O(n^2) means the time to complete grows quadratically as the input size grows.


# Introduction to Recursion in Python
# Recursion is a technique where a function calls itself within its definition.

def factorial(n):
    print(n)
    if n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
result = factorial(5)
print("Factorial of 5 is:", result)

#----------------------------------------------------
# CODE EXAMPLE: SUM OF A LIST USING RECURSION
#----------------------------------------------------

def sum_of_list(lst, n):
    if n == 0:
        return 0
    return lst[n-1] + sum_of_list(lst, n-1)

result = sum_of_list([1, 2, 3, 4, 5], 5)
print("Sum of list is:", result)

#------------with detailed explanation--------------
def sum_of_list(lst, n):
    print(f"Calculating sum of first {n} elements of {lst}")
    if n == 0:
        print("Reached base case: sum is 0")
        return 0
    result = lst[n-1] + sum_of_list(lst, n-1)
    print(f"Sum of first {n} elements is {result}")
    return result
    
# Running the step-by-step example
result = sum_of_list([1, 2, 3], 3)
print(f"Final Output: Sum of list is {result}")

#------------with detailed explanation--------------
def sum_of_list(lst, n):
    print(f"Calculating sum of first {n} elements of {lst}")
    if n == 0:
        print("Reached base case: sum is 0")
        return 0
    print("element getting added is ::",lst[n-1])
    result = lst[n-1] + sum_of_list(lst, n-1)
    print(f"Sum of first {n} elements is {result}")
    return result
    
# Running the step-by-step example
result = sum_of_list([5, 3, 66, 46, 12], 5)
print(f"Final Output: Sum of list is {result}")

#------------with detailed explanation--------------
#-------------try to improve the code for boundary conditions
#------------------------------------------------------------

 
