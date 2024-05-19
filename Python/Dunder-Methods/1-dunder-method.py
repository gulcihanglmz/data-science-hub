from typing import Iterable


print(3+8)
print(int.__add__(3,8))
 
print("Maria","James")
print("Maria"+"James")
print(str.__add__("Maria","James"))

print([1,2,3]+[4,5,6])
print(list.__add__([1,2,3],[4,5,6]))


class myList(list):
    def __add__(list1,list2):  #add function is defined in the list class so we can do it override 
        if len(list1) != len(list2):
            print("This items cannot be added")
        else:
            result = myList()
            for i in range(len(list1)):
                result.append(list1[i]+list2[i])
        return result
    
    
    def __sub__(list1,list2):  #subtraction is not defined in the list class so we cannot override
        if len(list1) != len(list2):
            print("This items cannot be subtracted")
        else:
            result = myList()
            for i in range(len(list1)):
                result.append(list1[i]-list2[i])
        return result
    
    
    def __eq__(list1,list2) :
        if sum(list1) == sum(list2):
            return True
        return False
    
    
    def __abs__(list):
        result = myList()
        for i in list:
            if i >=0:
                result.append(i)
            else:
                result.append(-1*i)
        return result
    
list1 = myList([10,11,12])
list2 = myList([14,15,16])
list3 = myList([-5,-42,9])

print(list1+list2)
print(list1-list2)
print(list1==list2)

print(abs(list3))

