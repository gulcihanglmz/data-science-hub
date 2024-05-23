#map ve filter gibi bir fonk. ve bir liste alır
#farkı sadece bir değer döndürüyor

from functools import reduce

list1 = [2,4,6,9]
def summation(x,y):
    return x+y
def mult(x,y):
    return x*y

result1 = reduce(summation,list1)
print(result1)

result2 = reduce(mult,list1)
print(result2)

result3 = reduce(lambda x,y : x+y ,list1)
result4 = reduce(lambda x,y : x*y ,list1)
print(result3)
print(result4)
