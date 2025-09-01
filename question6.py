# *_ _ _ _ _*
# *_ _ _ _*
# *_ _ _*
# *_ _*
# *_*

n = int(input("enter a number : "))
for i in range(1,1+n):
    print("*",end=" ")
    for j in range(n-i):
        print(" ",end="")
    if i!=n:
        print("*",end="")
    print()        
