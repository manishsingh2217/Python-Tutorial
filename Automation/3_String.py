# Strings in python are surrounded by either single quotation marks, or double quotation marks.

print('hello am single quoted')
print("hello I am double qutoted")
print('''hello I am triple quoted''')
print("He is called 'Manish Singh'")

# multiline string in python
a= """Hello I am 'Manish singh'
I  am a B.Tech 2nd year student"""
print(a)

#  strings in Python are arrays of bytes representing unicode characters.
print(a[6])  # printing 6th index of array or string 

# looping through string
for x in a:
    print(x)
        
#string length  using len function
name ="Manish singh"
print(len(name)) 


#To check if a certain phrase or character is present in a string, we can use the keyword 'in'
print("Manish singh" in a)

#To check if string end with "specific string"
print(a.endswith("rr"))

#to count the number of frequency of any string
print(a.count("M"))

# to captalize the first charcter
print(a.capitalize())

# to find the specific string in other string and retuen string 
print(a.find("singh"))