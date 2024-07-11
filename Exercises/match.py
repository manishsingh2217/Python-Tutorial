char = input("Enter operation you want to perform : ")
num1=int(input("Enter number 1 : "))
num2=int(input("Enter number 2 : "))
match char:
    case '+':
        print(num1+num2)
    case'-':
        print(num1-num2)
    case '*':
        print(num1*num2)    