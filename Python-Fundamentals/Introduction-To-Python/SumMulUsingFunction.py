#function returning multiple values
#Program to find sum and mutiplication of 2 number using function
def calculation(x,y):
    sum = x+y
    mul = x*y
    return (sum,mul)

a = int(input("Enter first number: "))
b = int (input("Enter second number: "))
s, m = calculation(a,b)
print(f'Sum of {a} and {b} is  {s} and multipliction is {m}')
