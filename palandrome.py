x=int(input("Enter any number :"))
y = x
z = 0
while y > 0:
    a = y % 10
    z = (z * 10) + a
    y = y // 10
if x == z:
  print('Palindrome')
else:
  print("Not Palindrome")
