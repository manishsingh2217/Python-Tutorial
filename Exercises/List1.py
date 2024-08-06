var = ['hello','Manish','bhai']
print(var)

# blank list
listBlank=[]
print("Printing blank list : ",listBlank)

# adding element to list
listBlank.append(2)
print("2 added to list using append meathod : ",listBlank)
var.append(5)
print("5 added to list using append meathod : ",var)

# adding element to desired place
var.insert(1,34)
print(var)

# adding more element at one time in python
listBlank.extend([2,4,3,2,4,5,5,6,7,7])
print("Added more element using extend meathod : ",listBlank)