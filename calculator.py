x=int(input("Enter any number : "))
y=int(input("Enter any number : "))
z=int(input("Enter 1 to add , 2 to subract , 3 to divide and 4 to multiple the entered numbers : "))
if z==1 :
    print("The sum of the entered numbers is : ")
    print(x+y)
elif z== 2 :
    print("The difference of the entered numbers is : ")
    print(x-y)
elif z== 3 :
    print("The quotient of the entered numbers is : ")
    print(x/y)
elif z== 4 :
    print("The product of the entered numbers is : ")
    print(x*y)
else :
    print("The input is invalid  , please try again")
