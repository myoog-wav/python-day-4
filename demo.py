'''
review of functions. Function is a reusable block of code that does a specific task. Built in functions 
and user-defined functions.

Methods.

functions you write differently.

Everything is an object. name = "sam" is a object.

so its a function built into a object. So for strings, there lower(), upper() which attaches itself to an objewct.

so you call the variable name and add a . to call a method.

'''

name = 'sam'

upper_name= name.upper()

string_example = "Woah piano tuba."

string_example = string_example.replace("tuba", "woah")

print(string_example)

groceries = "apple bread apple apple bread bread bread"

groceries = groceries.count("e")

print(groceries)

# username = input("What is your usersame?")
# username = username.strip
# if username == "Sam":
    # print("You have a account")

'''
    
    ------------

Python Data structures

List
Tuple
Dictionary

collections of data. 

Lists and Dictionaries.

lists are sqaure brackets. Elements in a data struc

    
    
    
    
'''

empty_list = []

grocery_list = ["apples", "bread", "pizza", 6, True, "pizza"]
second_list = [[1, 2], [3, 4, 5]] # List in a list lol.

students = ["Huck", "Ishan", "Pooja", "Tyler", "Sam"]
print(students[0])

# Methods. append() whichs adds at the end of the list.

students.append("Rob")
print(students)

print(students.count("Huck"))

# clear() which can remove somethinng.
# copy()
# count()
# find the index of an element. .index
# reverse, which reverses the lists.
# sort(), sorts via alphabet.
# reverse and sort. can stack them.
# remove() can remove an item with a value.
# pop() removes element based off of index. depends on what information you have.

# lists are ordered, helps with ques. like signups, or a videogame is hitting a bunch of buttons to see if they hit a combo.

# ---------------------- Dictionary

empty_dictionary = {}

# mak3s a key / value pair. Multiple information about same object.

Cars = {
    "Brand" : "Ford", 
    "model" : "Mustang",
    "Year" : 1964,
    "Color" : "Blue",
    "Status" : "For sale"
    }

print(Cars["Color"]) # Put in the key, return the value. Color is the key, blue is the calue. 

'''
Dic methods

keys() returns a list with all the keys.
values()

Lists are orders,
dictionary have key value. doesn't have index, can only acess with key.




'''


'''
While loop.




'''

while True:
    name = input("has? ")
    if name == "Sam":
        print(1)
        break

count = 10
while count >= 1:
    print(count)
    count = count - 1

# For Loop is useful for going through something one by one.

students = ["Sam", "Huck", "Wow"]

for student in students:
    if student == "Huck":
        print(student)
long_string = "I love this so much i want to prgam forever."

for each_charector in long_string:
    print(each_charector)
