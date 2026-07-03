"""
=========================================================
                    map() Function in Python
=========================================================

Definition:
-----------
The map() function applies a given function to every item in an iterable
(like a list, tuple, or set) and returns a map object (iterator).

It is commonly used to transform or modify each element without writing
an explicit loop.

Syntax:
-------
map(function, iterable)

Parameters:
-----------
1. function  -> The function to apply to each element.
2. iterable  -> The sequence (list, tuple, etc.) to process.

Returns:
--------
A map object (iterator), which is usually converted into a list.

=========================================================
Example 1: Using a Normal Function
=========================================================
"""

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]

result = list(map(square, numbers))

print("Original List :", numbers)
print("Squared List  :", result)


"""
Output:
Original List : [1, 2, 3, 4, 5]
Squared List  : [1, 4, 9, 16, 25]
"""


# =========================================================
print("\n================ Example 2: Using Lambda =================\n")

numbers = [10, 20, 30, 40, 50]

double = list(map(lambda x: x * 2, numbers))

print("Original List :", numbers)
print("Doubled List  :", double)

"""
Output:
Original List : [10, 20, 30, 40, 50]
Doubled List  : [20, 40, 60, 80, 100]
"""