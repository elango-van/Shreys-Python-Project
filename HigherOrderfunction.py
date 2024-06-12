items = [1,2,3,4,5]
double_items = []

""""
for i in items:
    double_items.append(i*2)

print(double_items)


def doubled(n):
    return n*2

double_items = map(doubled, items)
double_items = list(double_items)
print(double_items)

doubled_list = list(map(lambda x:x*2, items))
print(doubled_list)


#filter(function, iterable)

def isEven(n):
    return n%2 == 0

even_nums = filter(isEven,items);
print(list(even_nums))
"""

#Multiply numbers in a list
from functools import reduce

#result = reduce(lambda x,y: x*y, items)
result = reduce(lambda x,y: x*y, items, 2)
print(result)
