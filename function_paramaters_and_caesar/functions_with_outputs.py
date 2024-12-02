"""
We've seen functions with only an execution body, 
functions with inputs that allow for variation in execution of the function body, 
and now we'll see the final form of functions. Functions that can have outputs.

PAUSE 1
Create a function called format_name() that takes two inputs: f_name and `l_name'.

"""
def format_name(f_name, l_name):
    """
    Her kan man skrive doclines
    """
    pass

"""


Use the title() function to modify the f_name and l_name parameters into Title Case.

Syntax
You can create a function with a body, input and output like this:

def function_name(input_parameter):
    <body of function that uses input_argument>
    return output
Print vs. Output
Return vs. Display: 
The return statement is used to give back a value from a function, 
which can be used later, while print is used to display a value to the console only for the programmer to see.

"""

#Multiple return values

"""
Functions terminate at the return keyword. If you write code below the return statement that code will not be executed.

However, you can have multiple return statements in one function. So how does that work?

Conditional Returns
When we have control flow, as in the code will behave differently (go down different execution paths) depending on certain conditional checks, we can end up with multiple endings (returns).

e.g.

def canBuyAlcohol(age):
    if age >= 18:
        return True
    else:
        return False
Empty Returns

You can also write return without anything afterwards, and this just tells the function to exit.

e.g.

def canBuyAlcohol(age):
    # If the data type of the age input is not a int, then exit.
    if type(age) != int:
        return

    if age >= 18:
        return True
    else:
        return False
        """

"""Write a program that returns True or False whether if a given year is a leap year.

A normal year has 365 days, leap years have 366, with an extra day in February. 
The reason why we have leap years is really fascinating, this video does it more justice.


This is how you work out whether if a particular year is a leap year. 

- on every year that is divisible by 4 with no remainder

- except every year that is evenly divisible by 100 with no remainder 

- unless the year is also divisible by 400 with no remainder
"""
def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    if year%4 == 0:
        if not year%100 == 0:
            return True
    if year%100 == 0 and year%400 == 0:
        return True
    else:
        return False
            
#print(is_leap_year(2100))
