age=int(input("Enter your age : "))
Day=input("Enter the what is day today : ")

if Day=="Wednesday" or Day=="wednesday":
    if age>=18:
        print("Your ticket price is 10$")
    else:
        print("Your ticket price is 6$")
else:
    if age >=18:
        print("Your ticket price is 12$")
    else:
        print("Your ticket price is 8$")
        
        
#same program

Age=int(input("Enter your age : "))
price=2 if age>=18 else 8

if Day=="Wednesday" or Day=="wednesday":
    if age>=18:
        print("Your ticket price is 10$")
    else:
        print("Your ticket price is 6$")
else:
    if age >=18:
        print("Your ticket price is 12$")
    else:
        print("Your ticket price is 8$")