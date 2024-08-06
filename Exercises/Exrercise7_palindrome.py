number = int(input("Enter the numeber : "))
sum=0
temp =number
while(number != 0):
    rem=number%10
    sum=(sum*10)+rem
    number=number//10
if sum==temp:
    print(sum," is palindrome number")
else:
    print(sum," is not a palindrome number")        

