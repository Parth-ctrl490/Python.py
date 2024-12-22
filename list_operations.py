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



