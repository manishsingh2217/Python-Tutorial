file = open('C:\\Users\\Manish singh\\Desktop\\Python Tutorial\\Exercises\\Exercise1_listDir.py','r')
data =file.read()
print(data)
file.close()



# read with split lines

file1 = open('C:\\Users\\Manish singh\\Desktop\\Python Tutorial\\Exercises\\Exercise3_DetectSpace.py','r')

data1=file1.read().splitlines()
print(data1)

# readline() read a single line
print("Reading single line from file")
data2=file1.readline().splitlines()
print(data2)
file1.close()
