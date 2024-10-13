#recursive function
def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fact(num-1)

digit = int(input("Enter any mumber: "))
print (f"factorial of {digit} is : ", fact(digit))
