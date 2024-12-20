# Python Programming Tutorial

# Printing and Comments
# Printing is a fundamental operation to display output to the console.
print("hello world")  # Printing statement

# Comments
# Comments are used to explain code and are ignored by the Python interpreter.
# Single-line comments use the '#' symbol.
'''Multiline comments
can be written using triple single quotes.'''

# Operators in Python
# Operators are special symbols used to perform operations on variables and values.
# Arithmetic operators: +, -, *, /, %, ** (exponentiation), // (floor division)
# Assignment operators: =, +=, -=, *=, /=, etc.
# Comparison operators: ==, !=, >, <, >=, <=
# Logical operators: and, or, not

# Type Casting and type() Function
# Type casting is converting one data type to another.
a = 13  # Integer type
print(type(a))  # Output: <class 'int'>

b = "13"  # String type
print(type(b))  # Output: <class 'str'>

# Datatypes
# Datatypes are used to define the type of data a variable can hold.
# String
str = "Parth Shukla"
print(str)

# Integers
age = 20
print(age)

# Float
weight = 60.3
print(weight)

# Input() Function
# The input() function is used to take user input as a string.
name = input("Enter your name:")

# Slicing
# Slicing is used to access a range of characters in a string.
a = "parth"
print(a[0:3])  # Output: 'par'
print(a[1:3])  # Output: 'ar'

word = "amazing"
print(word[1:6:2])  # Output: 'mzn'

# String Functions
# Python provides several built-in methods to manipulate strings.
str = "Parth"
print(str.upper())  # Convert string to uppercase
print(len(str))  # Find length of string
print(str.endswith("rth"))  # Check if string ends with specified substring
print(str.count("a"))  # Count occurrences of a character
print(str.capitalize())  # Capitalize first letter
print(str.find("h"))  # Find position of a character
print(str.replace("r", "l"))  # Replace occurrences of a substring

# Arithmetic Operators
# Perform mathematical operations
print("The value of 10 + 20 is", 10 + 20)
print("The value of 10 - 20 is", 10 - 20)
print("The value of 10 * 20 is", 10 * 20)
print("The value of 10 / 20 is", 10 / 20)
print("The value of 10 % 20 is", 10 % 20)  # Modulus
print("The value of 10 ** 20 is", 10 ** 20)  # Exponentiation
print("The value of 10 // 20 is", 10 // 20)  # Floor division

# Multiline String
# Multiline strings can be created using triple quotes.
mls = '''Hi, my name is Parth Shukla 
and I am 20 years old.'''
print(mls)

# End Parameter
# The end parameter in print() specifies the string to append after the output.
print("This is print statement 1", end=" ")
print("This is print statement 2")

# Lists
# Lists are ordered, mutable collections of items.
colleges = ['IIT', 'NIT', 'BITS']
print(colleges[0])  # Accessing elements

colleges = "Psit"
print(colleges[2])  # Access character in string
print(colleges)

# Append in Lists
list1 = ['table', 'chair', 'clothes', 'pen', 'copy']
list1.append('book')
print(list1)  # Adds 'book' at the end of the list

# Insert in Lists
list1.insert(3, 'pencil')
print(list1)  # Inserts 'pencil' at index 3

# Remove in Lists
list1.remove('pencil')
print(list1)  # Removes 'pencil' by value

# Pop in Lists
list1.pop(3)
print(list1)  # Removes element at index 3

# Len, Max, and Min
# These functions are used to find the length, maximum, and minimum values.
list2 = ['car', 'bike', 'truck', 'cycle']
print(len(list2))  # Length of the list
print(max(list2))  # Max value alphabetically
print(min(list2))  # Min value alphabetically

# Tuples
# Tuples are immutable, ordered collections of items.
a = ()  # Empty tuple
a = (1,)  # Single element tuple
a = (1, 7, 2)  # Multiple elements

tup = (1, 2, 3, 4, 5)
print(tup[0])  # Accessing elements

# Convert Tuple to List
tup2 = (2, 3, 4)
list3 = list(tup2)
print(list3)

tup3 = (4, 7, 8)
print(len(tup3))  # Length of the tuple
print(max(tup3))  # Max numerical value
print(min(tup3))  # Min numerical value

# Dictionaries
# Dictionaries store data as key-value pairs.
dict1 = {'name': 'Parth', 'age': 20, 'city': 'Kanpur'}
print(dict1['name'])

# Update Value in Dictionary
dict1['name'] = 'Rahul'
print(dict1)
print(dict1.keys())  # Keys in the dictionary
print(dict1.values())  # Values in the dictionary
print(dict1.items())  # Key-value pairs
print(dict1.get('name'))  # Access using get method

# Sets
# Sets are unordered collections with no duplicate elements.
s = set()  # Empty set
s.add(1)
s.add(2)

s = {1, 8, 3, 2}
print(len(s))  # Length of the set
s.remove(8)  # Remove element
print(s)
s.pop()  # Remove arbitrary element
print(s)
s.clear()  # Remove all elements
print(s)
s = {1, 8, 3, 2}
print(s.union({8, 11}))  # Union of sets

# Conditional Expressions
# Conditional statements control the flow of execution.
if 5 > 3:
    print("5 is greater than 3")
else:
    print("5 is less than 3")

# Loops
# While Loop
# Executes code while a condition is true.
i = 0
while i < 50:
    print("Parth")
    i += 1

# For Loop
# Used to iterate over a sequence.
l = [1, 7, 8]
for item in l:
    print(item)

# Range
for i in range(0, 7):
    print(i)

# For Loop with Else
for item in l:
    print(item)
else:
    print("done")

# Break Statement
# Terminates the loop.
for i in range(0, 80):
    print(i)
    if i == 3:
        break

# Continue Statement
# Skips the current iteration.
for i in range(4):
    print("printing")
    if i == 2:
        continue
    print(i)

# Pass Statement
# Used as a placeholder in code blocks.
for item in l:
    pass

# Functions
# Functions are reusable blocks of code.
def func1():
    print('hello')

def greet(name):
    gr = "hello " + name
    return gr

a = greet("Parth")  # "hello Parth"

def greet_default(name="stranger"):
    print("hello", name)

def factorial(n):
    # Recursive function to calculate factorial
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# File I/O
# File handling involves reading and writing to files.
# Open a file
f = open("this.txt", "r")
text = f.read()
print(text)
f.close()

# Writing Files
f = open("this.txt", "w")
f.write("This is nice")
f.close()

# Using With Statement
# Automatically handles closing of files.
with open("this.txt", "r") as f:
    text = f.read()
    print(text)

# Object-Oriented Programming (OOP)
# OOP is a paradigm based on objects and classes.
class Employee:
    company = "Google"

    def __init__(self, name):
        self.name = name

    def get_salary(self):
        print("Salary not specified")

    @staticmethod
    def greet():
        print("Hello, World!")

Parth = Employee("Parth")
print(Parth.company)
Parth.get_salary()
Parth.greet()

# Exception Handling
# Exception handling allows a program to handle errors gracefully.
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Invalid input. Please enter a number.")
finally:
    print("Execution completed.")
