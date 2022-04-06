# PYTHON SYNTAX CHEAT SHEET

# The first time a module is loaded into a running Python script, it is
# initialized by executing the code in the module once. If another module
# in your code imports the same module again, it will not be loaded twice
# but once only - so local variables inside the module act as a "singleton"
# - they are initialized only once.

import urllib.request  # allows requesting urls

# In Python 3, print is a function
print("Hello World")

# Python uses indentation for blocks, instead of curly braces. Both tabs and spaces are supported.
x = 1
if x == 2:
    print("inside if")
print("outside if")

# Python is completely object oriented, and not "statically typed".
# You do not need to declare variables before using them, or declare their type. Every variable in Python is an object.
myfloat = 1.0 + float(1)
print(myfloat + 1)  # two types of numbers - integers and floating

# Assignments can be done on more than one variable "simultaneously"
one, two = 1, 2
print("One + Two = ", one + two)

# Lists are very similar to arrays. They can contain any type of variable.
fruits = ["apple", "banana"]
fruits.append("orange")
fruits.append(55)

for fruit in fruits:
    print(fruit)

print("List of fruits: %s" % fruits)

for i in range(3):
    print("iFruit: %s" % (fruits[i]))

# Funky condictionals
if "tomato" in fruits:
    print("tomato is in the basket")
elif "letuce" in fruits:
    print("letuce is in the basket")
else:
    print("none in the basket")

# Conditional gotchas!
if not "":
    print("gotcha: empty string")
if not []:
    print("gotcha: empty list")
if not 0:
    print("gotcha: zero is true")

stringOne = "Hello"
stringTwo = "Hello"

print("String comparison: %s " % (stringOne is stringTwo))

# String  tricks
astring = "Hello world!"
length = len(astring)
oindex = astring.index("o")
substring = astring[6:11]
astringReversed = astring[::-1]

print("%s, length=%d, o index=%d, substring=%s, reversed=%s" %
      (astring, length, oindex, substring, astringReversed))

# Functions


def personalized_motd(username, greeting):
    return "Howdy %s! Wish you %s" % (username, greeting)


print(personalized_motd("John", "Good morning"))

# Classes


class Person:
    name = "no name"

    def function(self):
        print("This is a message inside the class")


filipe = Person()
filipe.name = "Filipe"
filipe.function()

# Dictionaries (funky type of HashMaps)
phonebook = {}
phonebook["Ana"] = 123456789
phonebook["Bob"] = 987654321
phonebook["Claudia"] = 123498765

salaries = {
    "Ana": 10000,
    "Bob": 11000
}

phonebook.pop("Bob")
del phonebook["Claudia"]

for name, phone in phonebook.items():
    print("%s's phone is %s" % (name, phone))

if "Ana" in phonebook:
    print("Ana is still in the phonebook")

# In the Python console you can use dir(urllib) or help(urllib) to retrive the list of methods
url = (urllib.request.urlopen("http://www.google.com"))
html = url.read()
print(html[0:50])

# Exception handling
try:
    print(uninitialized)
except:
    print("Caught a runtime exception")

# Writing modules
# To create a module of your own, simply create a new .py file with the module name, and then import
# it using the Python file name (without the .py extension) using the import command.

# Writing packages
# Packages are namespaces which contain multiple packages and modules themselves. They are simply
# directories, but with a twist.Each package in Python is a directory which MUST contain a special file
# called __init__.py. This file can be empty, and it indicates that the directory it contains is a Python
# package, so it can be imported the same way a module can be imported.
