"""
Local Scope:
Variables (or functions) declared inside functions have local scope (also called function scope). They are only seen by other code within the same block of code.

e.g.

def my_function():
    my_local_var = 2
    
# This will cause a NameErrorr
print(my_local_var)

Global Scope:
Variables or functions declared at the top level (unindented) of a code file have global scope. It is accessible anywhere in the code file.

e.g.

my_global_var = 3

def my_function():
    # This works no problems
    print(my_global_var)
"""

"""
Block scope

Python is a bit different from other programming languages in that it does not have block scope.

This means that variables created nested in other blocks of code e.g. 
for loops, if statements, while loops etc. don't get local scope. They are given 
function scope if they are within a function or global scope if they are not.

e.g.

# Accessible anywhere
my_global_var = 1

def my_function():
    # Only accessible within my_function()
    my_local_var = 2
    
for _ in range(10):
    # Accessible anywhere
    my_block_var = 3
"""

