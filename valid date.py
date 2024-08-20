list31=['1' , '3' , '5' , '7' , '8' , '10' , '12' ]
list30=['2' , '4' , '6' , '9' , '11' ]
x=int(input("Enter the day of the month : "))
y=int(input("Enter the month of the year : "))
z=int(input("Enter the year : "))
if z<=0 :
    print("Entered year is wrong")
elif y<=0 or y>12 :
    print("Entered month is wrong")
elif y==list31 and x>31 :
    print("Entered date is wrong")
elif y==list30 and x>30 :
    print("Entered date is wrong")
elif y==2 and x>28 :
    print("Entered date is wrong")
else :
    print("The entered date is correct")
