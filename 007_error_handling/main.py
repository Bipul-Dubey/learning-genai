"""
=========================================================
                Error Handling in Python
=========================================================

Definition:
-----------
Error handling is the process of detecting and handling errors that occur
during the execution of a program so that the program does not crash.

Python provides the try, except, else, and finally blocks to handle
exceptions gracefully.

Syntax:
-------

try:
    # Code that may raise an exception
except ExceptionType:
    # Code to handle the exception
else:
    # Executes if no exception occurs
finally:
    # Always executes (whether an exception occurs or not)

=========================================================
Example 1: try and except
=========================================================
"""

try:
    num = 10
    result = num / 0
    print(result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

"""
Output:
Error: Cannot divide by zero.
"""


# =========================================================
print("\n================ Example 2: Multiple Exceptions =================\n")

try:
    number = int("abc")
    result = 10 / number

except ValueError:
    print("ValueError: Invalid number.")

except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero.")

"""
Output:
ValueError: Invalid number.
"""


# =========================================================
print("\n================ Example 3: Generic Exception =================\n")

try:
    my_list = [1, 2, 3]
    print(my_list[5])

except Exception as e:
    print("Error:", e)

"""
Output:
Error: list index out of range
"""


# =========================================================
print("\n================ Example 4: try-except-else =================\n")

try:
    a = 20
    b = 4
    result = a / b

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Division Successful")
    print("Result =", result)

"""
Output:
Division Successful
Result = 5.0
"""


# =========================================================
print("\n================ Example 5: try-except-finally =================\n")

try:
    file = open("sample.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File does not exist.")

finally:
    print("Program execution completed.")

"""
Output (if file doesn't exist):
File does not exist.
Program execution completed.
"""


# =========================================================
print("\n================ Example 6: try-except-else-finally =================\n")

try:
    num = 50
    result = num / 5

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result =", result)

finally:
    print("This block always executes.")

"""
Output:
Result = 10.0
This block always executes.
"""


# =========================================================
print("\n================ Example 7: Raising an Exception =================\n")

age = -5

try:
    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Age =", age)

except ValueError as e:
    print("Error:", e)

"""
Output:
Error: Age cannot be negative.
"""


# =========================================================
print("\n================ Example 8: User Defined Exception =================\n")

class InvalidAgeError(Exception):
    pass

try:
    age = 15

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")

    print("Eligible")

except InvalidAgeError as e:
    print("Custom Exception:", e)

"""
Output:
Custom Exception: Age must be 18 or above.
"""


# =========================================================
print("\n================ Common Built-in Exceptions =================\n")

print("""
1. ZeroDivisionError
   -> Division by zero.

2. ValueError
   -> Invalid value passed.

3. TypeError
   -> Wrong data type.

4. IndexError
   -> Invalid list index.

5. KeyError
   -> Dictionary key not found.

6. FileNotFoundError
   -> File does not exist.

7. NameError
   -> Variable not defined.

8. AttributeError
   -> Object has no requested attribute.

9. ImportError
   -> Module cannot be imported.
""")


# =========================================================
print("\n================ Quick Revision =================\n")

print("""
Definition:
Error handling allows a program to continue running even if an error occurs.

Keywords:
✔ try
✔ except
✔ else
✔ finally
✔ raise

Flow:
try
   ↓
Exception?
   ↓
Yes ---------> except
No ----------> else
        ↓
     finally (Always Executes)

Interview Points:
✔ try contains risky code.
✔ except handles exceptions.
✔ else runs only if no exception occurs.
✔ finally always executes.
✔ raise is used to create an exception manually.
✔ Custom exceptions are created by inheriting Exception.
""")