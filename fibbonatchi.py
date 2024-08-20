n = int(input("Enter the number of terms :"))
x = 0
y = 1
z = y  
i = 1
while i <= n:
    print(z, end=" ")
    i += 1
    x, y = y, z
    z = x + y
print()
