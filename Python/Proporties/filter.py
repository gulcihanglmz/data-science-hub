#filter : parametere olarak bir fonk. bir de liste alıyor (map gibi)
#fonksiyon true veya false değer döndüren bir fonk. olmalı

list1 = [1,2,3,5,8,7,11,123,9]

def isEven(x):
    if x %2 == 0:
        return True
    return False
evenNumbers = list(filter(isEven,list1))
print(evenNumbers)

def two_digit(x):
    if x>=10 and x<100:
        return True
    return False

twoDigit = list(filter(two_digit , list1))
print(twoDigit)


#with lambda
evenNumbers = list(filter(lambda x : x%2 ==0 ,list1))
print(evenNumbers)

twoDigit = list(filter(lambda x :x>=10 and x<100 , list1))
print(twoDigit)


list2 = [1,5,(4,8,9),True , "Python","Java","Kotlin",{5,4,3}]
strings = list(filter(lambda x : isinstance(x,str) , list2))
bools = list(filter(lambda x : isinstance(x,bool) , list2))
print(strings)
print(bools)

