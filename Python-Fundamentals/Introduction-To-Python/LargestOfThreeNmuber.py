#largest of 3 number
a = int(input("Enter first number: "))
b = int(input("Enter first number: "))
c = int(input("Enter first number: "))
if a>b and a>c:
    print(a, " is largest number.")
elif b>a and b>c:
    print(b, " is the largest number.")
else:
    print(c, " is the largest number.")
