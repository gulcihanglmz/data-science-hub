
list1 = [1,2,3,4,5,6,7,8,9]
list2 = []
for i in list1:
    list2.append(i)
print(list2)

#list comprehension
list3 = [number for number in list1]
print(list3)


list4 = [number**2 for number in list1]
print(list4)

list5 = [number for number in list1 if number %2==0]
print(list5)

list6 = [number**2 for number in list1 if number %2==0]
print(list6)

list7 = [number**2 for number in list1 if number>4 and number %2==0]
print(list7)


#
numbers = [1,2,3]
letters = ["a","b"]
list8 = []
for number in numbers:
    for letter in letters:
        list8.append((number,letter))
print(list8)

#with list comprehension
list9 = [(number,letter) for number in numbers  for letter in letters ]
print(list9)

#
num1 = [1,2,5,8,7,9,10]
num2 = [2,8,9]
num3 = []
for i in num1:
    if i not in num2:
        num3.append(i**2)
print(num3)

num4 = [(i**2) for i in num1 if i not in num2]
print(num4)


#
list_ = [[1,2,3],[4,5,6,7],[8,9,10,11,12]]
list2_ = []
for i in list_:
    for j in i:
        list2_.append(j)
print(list2_)

list3_ = [j  for i in list_ for j in i ]
print(list3_)
