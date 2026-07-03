"""
=========================================================
                  filter() Function in Python
=========================================================

Definition:
-----------
The filter() function is used to select elements from an iterable
(like a list, tuple, or set) based on a condition.

It keeps only those elements for which the function returns True.

Syntax:
-------
filter(function, iterable)

Parameters:
-----------
1. function  -> A function that returns True or False.
2. iterable  -> The sequence (list, tuple, etc.) to filter.

Returns:
--------
A filter object (iterator), which is usually converted into a list.

=========================================================
Example 1: Using a Normal Function
=========================================================
"""

def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(is_even, numbers))

print("Original List :", numbers)
print("Even Numbers  :", result)

"""
Output:
Original List : [1, 2, 3, 4, 5, 6]
Even Numbers  : [2, 4, 6]
"""


# =========================================================
print("\n================ Example 2: Using Lambda =================\n")

numbers = [10, 15, 20, 25, 30, 35]

multiples_of_10 = list(filter(lambda x: x % 10 == 0, numbers))

print("Original List      :", numbers)
print("Multiples of 10    :", multiples_of_10)

"""
Output:
Original List      : [10, 15, 20, 25, 30, 35]
Multiples of 10    : [10, 20, 30]
"""