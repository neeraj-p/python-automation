#fibonacci series 0,1,1,2,3,5,8,13
a, b = 0, 1
number = 10
i = 0
while (i<number):
    print(a, end=' ')
    a,b = b,a+b
    i+= 1
