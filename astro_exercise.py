nos = int(input("Enter any no between 1 to 10\n"))
fb = int(input("Enter 0 or 1"))
bull=bool(fb)
#
x=1
#
if bull==False:
    while nos>0:
        print(nos*"*")
        nos=nos-1
elif bull==True:
    while nos>0:
        print((nos-(nos-x))*"*")
        nos=nos-1
        x=x+1
