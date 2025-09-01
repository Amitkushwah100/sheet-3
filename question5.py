# *_ _ _*
# *_ _ _*
# *_ _ _*
# *_ _ _*
# *_ _ _*



n = int(input("enter a number : "))   
for i in range(1,1+n):
    for j in range(1,n+1):
        if(j==1) or (j==n):
            print("*",end=" ")
        else:
            print("_",end=" ")
    print()        