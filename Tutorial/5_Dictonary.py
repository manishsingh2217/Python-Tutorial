# it is a collection of key value pair
dict ={
    "Name":"Manish Singh",
    "Course":"B.Tech",
    "mark":[1,3,4,5,6,7]
}

print(dict)
print(dict["Name"])

# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

print(dict.items()) # return the list key values 

print(dict.keys()) #return the list of key 

dict.update({"Failed Student":["manish","Alok"]}) #it will update the dictionary with given pair of key and value

print(dict.keys())
print(dict.get("Failed Student"))

# set is a collection of non repetetive element
#  Set items are unchangeable, but you can remove items and add new items.
# Set items are unordered, unchangeable, and do not allow duplicate values.
set={"Manish singh","Priyanjali(Ziddi)","Saurabh singh","a","a"}

# Note: Sets are unordered, so you cannot be sure in which order the items will appear.

print(set)

set.add(5)
set.add(7)
print(set)
