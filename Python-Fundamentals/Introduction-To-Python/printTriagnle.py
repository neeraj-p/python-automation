#print a triange increasing order
for i in range(1,11):
    for j in range(i):
         print("*",end='')
    print("")
    
#print a triange decreaing order
n =11
for i in range(1,n):
    for j in range(1,n):
        if(j<n):
            print("#",end='')
    n=n-1
    print("")
