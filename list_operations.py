#Access list items
a=[10,20,30,40,50]
print(a[0])  # accessing the first element
print([a[-1]])#accessing the last element
 #output
#10
#50

#USING LOOP
a=[10,20,30,40,50]
for i in a:
    print(i)
    #output
    #10
    #20
    #30
    #40
    #50

#Using list comprehension
a=[10,20,30,40,50]
b=[i for i in a if i>20]
print(b)
#output
# [30, 40, 50]

#Using list slicing
a=[10,20,30,40,50]
print(a[1:4])
#output
# [20, 30, 40]


#change list items 1
a=[10,20,30,40,50]
print(a[0])
print(a[1])
print(a[-1])
#output
#10
#20
#50

# Example 1: Change Single list item.

# Approach:

# Change first element mylist[0]=value
# Change third element mylist[2]=value
# Change fourth element mylist[3]=value


List=[10,20,30,40,50,60]
print("Original list")
print(List)

List[0]=11
List[2]=21
List[2]=31
List[3]=41
List[4]=51
List[5]=61
print("\nList after changing elements")
print(List)
#output
# Original list
# [10, 20, 30, 40, 50, 60]
# List after changing elements
# [11, 20, 31, 41, 51, 61]

# Example 2: Changing all values using loops.
List=[10,20,30,40,50,60]
print("Original list")
print(List)

print("After incrementing each element of list by 2")  
for i in range(len(List)):
    List[i]=List[i]+2
    print(List)
    #output
    # Original list
    # [10, 20, 30, 40, 50, 60]
    # After incrementing each element of list by 2
    # [12, 22, 32, 42, 52, 62]

# Changing all values of a list using List comprehension.
List=[10,20,30,40,50,60]
print("Original list ")
print(List)
print("After incrementing list by 2")
list2=[i+2 for i in List]
print(list2)
#output
# Original list
# [10, 20, 30, 40, 50, 60]
# After incrementing list by 2
# [12, 22, 32, 42, 52, 62]

#REPLACING VALUES
#Replacing a single element in a list
l=['Parth','Nikhil','Kunal','Alekh','Roshni']
l[0]='Aashike'
print(l)
#output
# ['Aashike', 'Nikhil', 'Kunal', 'Alekh', '
# 'Roshni']
# l[0]='Aashike' is used to replace the first element of the list with

#using for loop
l=['Parth','Nikhil','Kunal','Alekh','Roshni']
for i in range(len(l)):
    if l[i]=='Parth':
        l[i]='Aashike'

    if l[i]=='Nikhil':
        l[i]='Shrey'
print(l)
#output
# ['Aashike', 'Shrey', 'Kunal', 'Alekh', 
# 'Roshni']



# Replace Values in a List using While Loop

# define list
l = ['Hardik', 'Rohit', 'Rahul', 'Virat', 'Pant']

i = 0
while i < len(l):
    # replace hardik with shardul
    if l[i] == 'Hardik':
        l[i] = 'Shardul'
    # replace pant with ishan
    if l[i] == 'Pant':
        l[i] = 'Ishan'
    i += 1
# print list
print(l)
#output
# ['Shardul', 'Rohit', 'Rahul', 'Virat',
# 'Ishan']

# Replace Values in a List using Lambda Function

# define list
l = ['Hardik', 'Rohit', 'Rahul', 'Virat', 'Pant']

# replace Pant with Ishan
l = list(map(lambda x: x.replace('Pant', 'Ishan'), l))

# print list
print(l)
#output
# ['Shardul', 'Rohit', 'Rahul', 'Virat',
# 'Ishan']

l=['Parth','Nikhil','Kunal','Alekh','Roshni']
i=l.index("Alekh")
l=l[:i]+['Aloo']+l[i+1:]
print(l)
#output
# ['Parth', 'Nikhil', 'Kunal', 'Aloo',
# 'Roshni']

#Append items in list
a=[2,3,4,5]
a.append(8)
print(a)
#output
# [2, 3, 4, 5, 8]
# Append items in list using extend() function
a=[2,3,4,5]
a.extend([6,7,8])
print(a)
#output
# [2, 3, 4, 5, 6, 7,
# 8]

#insert items to a list
fruit=['banana','guava','mango']
fruit.insert(1,'apple')
print(fruit)
#output
# ['banana', 'apple', 'guava',
# 'mango']

list = ['Sun', 'rises', 'in', 'the', 'east']
list.insert(0, "The")
print(list)
#output
# ['The', 'Sun', 'rises', 'in',
# 'the', 'east']

list1=[1,2,3,4,5,6,7,8]
element=13
beforeelement=3
index=list1.index(beforeelement)
list1.insert(index,element)
print(list1)
#output
# [1, 2, 3, 13, 4, 5,
# 6, 7, 8]

#Inserting a Tuple into the List
list1=[1,2,3,4,5,6,7,8]
numtuple=(4,5,6)
list1.insert(2,numtuple)
print(list1)
#output
# [1, 2, (4, 5, 6), 3, 4, 5, 6]

fruits = ['apple', 'banana', 'cherry']
fruits.insert(0, 'orange')
print(fruits)
 # Output: ['orange', 'apple', 'banana', 'cherry']

fruits = ['apple', 'banana', 'cherry']
fruits.insert(-1, 'orange')
print(fruits) 
# Output: ['apple', 'banana', 'orange', 'cherry']

my_list = [{'name': 'Alice', 'age': 30}, 
           {'name': 'Bob', 'age': 25}]
new_dict = {'name': 'Charlie', 'age': 40}
my_list.append(new_dict)
print(my_list)
# Output: [{'name': 'Alice', 'age': 30}, {'name': 'Bob
# ', 'age': 25}, {'name': 'Charlie', 'age': 40}]

list1=[1,2,3]
list2=[4,5,6]
list1=list1+list2
print(list1)
#output
# [1, 2, 3, 4, 5, 6]

list1=[1,2,3]
s={4,5,6}
list1.insert(3,s)
print(list1)
#output
# [1, 2, 3, {4, 5, 6}]

#Extending a list in python

list1=[1,2,3]
list2=[4,5,6]
#Method 1: Using the extend() method
list1.extend(list2)
print(list1)
#output
# [1, 2, 3, 4, 5, 6]


#Method 2: Using the '+' operator
list1=list1+list2
print(list1)
#output
# [1, 2, 3, 4, 5, 6]

#Method 3:Using += Operator
list1=[1,2,3]
list2=[4,5,6]
list1+=list2
print(list1)

#output
# [1, 2, 3, 4, 5, 6]


#Using Slicing
list1=[1,2,3]
list2=[4,5,6]
list1[len(list1):]=list2
print(list1)
#output
# [1, 2, 3, 4, 5, 6]

from itertools import chain

a=[1,2,3]
n=[4,5,6]
a.extend(chain(n))
print(a)
#output
#[1, 2, 3, 4, 5, 6]


#How to Remove Item from a List in Python
a=[10,20,30,40,50]
a.remove(30)
print(a)
#output
# [10, 20, 40, 50]

a=[10,20,30,40,50]
a.remove(30)
print(a)
#output
# [10, 20, 40, 50]

a=[10,20,30,40,50]
v=a.pop(1)
print(a)
print(v)
#output
# [10, 30, 40, 50]
# 20 is removed

a=[10,20,30,40,50]
del a[2]
print(a)
#output
# [10, 20, 40, 50]

a=[10,20,30,40,50,60,70]
del a[1:4]
print(a)
#output
# [10, 20, 70]

a=[10,20,30,40]
a.clear()
print(a)
#output
# []

a = [1, 2, 3, 4, 5]
a.clear()
print("List after clearing:", a)
#output
# List after clearing: []


a = [1, 2, 3, 4, 5]
# Reassign 'a' to a new empty list
a = []
# Print the current state of 'a'
print("List after reassignment:", a)
#output
# List after reassignment: []

a = [1, 2, 3, 4, 5]
del a[:]
print("List after using del:", a)
#output
# List after using del: []



# Basic Methods
# append(item)

# Adds an item to the end of the list.
# extend(iterable)

# Extends the list by appending elements from an iterable (e.g., another list).
# insert(index, item)

# Inserts an item at a specified index.
# remove(item)

# Removes the first occurrence of a specified item.
# pop(index=-1)

# Removes and returns the item at the specified index (default is the last item).
# clear()

# Removes all elements from the list.
# index(item, start=0, end=len(list))

# Returns the index of the first occurrence of a specified item.
# count(item)

# Returns the number of occurrences of a specified item.
# sort(key=None, reverse=False)

# Sorts the list in ascending order by default. You can customize using the key and reverse parameters.
# reverse()

# Reverses the order of the list in place.
# copy()
# Returns a shallow copy of the list.
# Other Operations
# Slicing:
# Extract portions of a list using [start:stop:step].

# Concatenation:
# Combine lists using + or extend with slicing.

# Repetition:
# Repeat lists using *.

# Utility Functions (Not List-Specific)
# These are built-in functions that work with lists:

# len(list)

# Returns the number of items in the list.
# max(list)

# Returns the largest element in the list.
# min(list)

# Returns the smallest element in the list.
# sum(list)

# Returns the sum of elements in the list (numeric).
# all(list)

# Returns True if all elements in the list are truthy.
# any(list)

# Returns True if at least one element in the list is truthy.
# enumerate(list, start=0)

# Returns an enumerate object containing index-value pairs.
# sorted(list, key=None, reverse=False)

# Returns a new sorted list (does not modify the original list).
# zip(*lists)

# Combines multiple lists into tuples.
# From itertools
# chain(*iterables)

# Combines multiple iterables into one.
# combinations(iterable, r)

# Returns all possible r-length combinations from the iterable.
# permutations(iterable, r)

# Returns all r-length permutations from the iterable.
# islice(iterable, start, stop, step)

# Slices an iterable like a list.



