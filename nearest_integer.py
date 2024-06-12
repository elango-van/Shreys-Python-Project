
def myround(x, base=5):
    return base * round(x/base)

print(myround(2546.2565))
print(myround(2556.2565,50))


lst=[ 1, 6, 3, 5, 3, 4 ]
#checking if element 7 is present
# in the given list or not
i=4
# if element present then return
# exist otherwise not exist
if i in lst:
    print("exist")
else:
    print("not exist")
