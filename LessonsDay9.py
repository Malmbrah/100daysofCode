#Dictonaries
"""
This is how you create a dictionary in Python:

# An example dictionary
colours = {
    "apple": "red", 
    "pear": "green", 
    "banana": "yellow"
}

This is how you retrieve items from a dictionary:

print(colours["pear"]) #Will print "green"

This is how to create an empty dictionary: my_empty_dictionary = {}

This is how you can add new items to an existing dictionary: colours["peach"] = "pink" #take care that you use the same type

This is also how you can edit an existing value in a dictionary: colours["apple"] = "green"

This is how to loop through a dictionary and print all the keys: 

for key in colours:
    print(key)

This is how to loop through a dictionary and print all the values:

for key in colours:
    print(colours[key])

You can wipe an existing dictionary by setting it to empty: dictionary = {}
"""

#Write a program that converts student scores to grades using a dictionary

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

#Går altså inn i student_scores og henter key med student og verdien deres
for student in student_scores:
    if 91 < student_scores[student] < 100:
        student_grades[student] = "Outstanding"
    
    elif 81 < student_scores[student] < 90:
        student_grades[student] = "Exceeds Expectations"
        
    elif 71 < student_scores[student] < 80:
        student_grades[student] = "Acceptable"
        
    elif student_scores[student] < 70:
        student_grades[student] = "Fail"
        
"""
Nesting a List inside a Dictionary
Instead of a String value assigned to a key, we can replace it with a List. You can nest a List in a Dictionary like this:

my_dictionary = {
    key1: [List],
    key2: Value,
}

1) See if you can figure out how to print out "Lille" from the nested List called travel_log.
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1])

"""

"""
--------------------------------------------------------------------------------------------------------------
Nesting Lists inside other Lists
We've previously seen Nested Lists:

nested_list = ["A", "B", ["C", "D"]]
2)
Do you remember how to get items that are nested deeply in a list? Try to print "D" from the list nested_list.

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])
"""
"""
---------------------------------------------------------------------------------------------------------------

Nesting a Dictionary inside a Dictionary
You can also nest a dictionary in a dictionary:

my_dictionary = {
    key1: Value,
    key2: {Key: Value, Key: Value},
}
PAUSE 3
Figure out how to print out "Stuttgart" from the following list:
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2])
"""
