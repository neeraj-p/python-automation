#print even number between 1 to n
n = int( input("Enter the number: "))
i = 1
sum = 0
while i<=n:
    if(i%2 == 0):
        sum = sum + i
    i+=1
print("sum of even number from 1 to ", n, "is : ", sum)
