"""
=========================================================
               Decorator Function in Python
=========================================================

Definition:
-----------
A decorator is a function that takes another function as an argument,
adds some extra functionality to it, and returns the modified function
without changing the original function's code.

In simple words:
A decorator allows you to extend or modify the behavior of a function
without editing the function itself.

Syntax:
-------
@decorator_name
def function_name():
    ...

Equivalent:

function_name = decorator_name(function_name)

=========================================================
Example 1: Basic Decorator
=========================================================
"""

def decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper


@decorator
def greet():
    print("Hello, Welcome!")

greet()

"""
Output:
Before calling the function
Hello, Welcome!
After calling the function
"""


# =========================================================
print("\n================ Example 2: Without @ Syntax =================\n")

def decorator(func):
    def wrapper():
        print("Starting...")
        func()
        print("Finished!")
    return wrapper


def display():
    print("Displaying data...")

display = decorator(display)

display()

"""
Output:
Starting...
Displaying data...
Finished!
"""


# =========================================================
print("\n================ Example 3: Decorator with Arguments =================\n")

def decorator(func):
    def wrapper(name):
        print("Before Function")
        func(name)
        print("After Function")
    return wrapper


@decorator
def greet(name):
    print(f"Hello {name}")

greet("Bipul")

"""
Output:
Before Function
Hello Bipul
After Function
"""


# =========================================================
print("\n================ Example 4: Logging Decorator =================\n")

def log(func):
    def wrapper():
        print("Function execution started.")
        func()
        print("Function execution completed.")
    return wrapper


@log
def task():
    print("Performing task...")

task()

"""
Output:
Function execution started.
Performing task...
Function execution completed.
"""


# =========================================================
print("\n================ Example 5: Timer Decorator =================\n")

import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Execution Time: {end - start:.4f} seconds")
    return wrapper


@timer
def process():
    time.sleep(1)
    print("Processing...")

process()

"""
Output:
Processing...
Execution Time: 1.000x seconds
"""


# =========================================================
print("\n================ Example 6: Authentication Decorator =================\n")

logged_in = True

def login_required(func):
    def wrapper():
        if logged_in:
            func()
        else:
            print("Access Denied!")
    return wrapper


@login_required
def dashboard():
    print("Welcome to Dashboard")

dashboard()

"""
Output:
Welcome to Dashboard
"""


# =========================================================
print("\n================ Quick Revision =================\n")

print("""
Definition:
A decorator is a function that adds extra functionality to another
function without modifying its original code.

Syntax:

@decorator_name
def function():
    ...

Equivalent:

function = decorator(function)

Uses:
✔ Logging
✔ Authentication
✔ Timing Execution
✔ Permission Checking
✔ Input Validation
✔ Caching

Advantages:
✔ Reusable
✔ Cleaner Code
✔ Avoids Code Duplication
✔ Easy to Maintain

Interview Points:
✔ A decorator is a function that accepts another function.
✔ It returns a new function with additional behavior.
✔ '@' is syntactic sugar for applying a decorator.
✔ Decorators are based on first-class functions and closures.
""")