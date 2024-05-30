# Lists are used to store multiple items in a single variable.
# Lists are created using square brackets
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

list = ["Manish","Saurabh","Ranju"]

# Accessing list item 
for x in list:
    print(x)

# using index method
print(list[0],list[1],list[2])    

# adding the item to existing list
# To add an item to the end of the list, use the append() method:
list.append("Sunil Singh")
print(list)

# To insert a list item at a specified index, use the insert() method.
# The insert() method inserts an item at the specified index
list.insert(2,"Priti Didi")
print(list)


# A list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]

# To append elements from another list to the current list, use the extend() method.
list.extend(list1)
print(list)

# list.sort
list3=[5,6,4,34,6,7,2,46]
list3.sort()
print(list3)

# it will the list 
list3.reverse()
print(list3)

#it will delete the element from index 2
list3.pop(2)
print(list3)

# it will the element 6 from list3 only frist occurence 
list3.remove(6)
print(list3)

# Tuples are written with round brackets
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

tuple = ("Manish singh","Alok chandel","Saurabh singh")
for x in tuple:
    print(x)