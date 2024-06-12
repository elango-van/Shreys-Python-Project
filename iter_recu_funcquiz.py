def myfunc(n):
     if n==1:
         return 0
     elif n==2:
         return  1
     else:
         return myfunc(n-1)+myfunc(n-2)

inp=int(input("Enter no for iter - "))
print("Answer - ",myfunc(inp))