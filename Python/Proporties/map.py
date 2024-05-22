#map fonksiyonu bir dizi veriyi başka bir diziye dönüştürür
#listedeki tüm elemanlara aynı işlemi uygulamak istiyorsak map kullanırız

list1 = [1,2,3,4,5,6]
def sqrFunct(x):
    return x**2
list2 = []
for i in list1:
    list2.append(sqrFunct(i))
print(list2)

#with map function 
#list = map(function , list)
list3 = list(map(sqrFunct, list1))
list4 = tuple(map(sqrFunct, list1))
print(list3) #list
print(list4) #tuple

#oluşan map objesi bir iterable'a (liste, tuple, vb.) dönüştürebiliriz

print("************************")

list5 = [7,6,5,4,3,2]
list6 = list(map(lambda x : x**2 , list5))   #map , bir funct bir de liste alır
list7 = tuple(map(lambda x : x**3 , list5))
print(list6)
print(list7)


#iki listeli map fonksiyonu
list8 = [2,4,6,8,10]
list9 = [1,3,5,7,9]
def summation(x,y):
    return x+y
result = list(map(summation,list8,list9))
print(result)

#en az eleman sayısına sahip listeye göre 
list8 = [2,4,6,8,10]
list9 = [1,3,5,7,9]
list10 = [5,4,7]
def summation(x,y,z):
    return x+y+z
result = list(map(summation,list8,list9,list10))
print(result)

#with lambda 
result2 = list(map(lambda x,y,z : x+y+z , list8 , list9 ,list10))
print(result2)


