#lamda : ismi olmayan fonksiyonlar tanımlamamıza yarıyor

def calculate_sqr(x):
    return x**2

#wth lamda 
sqr = lambda x : x**2
print(sqr) #function
print(sqr(5))

cube = lambda x : x**3 
print(cube(5))

summ = lambda x,y : x+y
print(summ(8,7))


summation = lambda *args : sum(args)
print(summation(5,7,8,5,9))


print((lambda x,y,z : x*y+z)(5,8,9))
print((lambda *args : sum(args))(2,5,6,3,4,7))


list1 = [("Ali",25),("Cenk",20),("Bahar",35),("Emel",22)]
list1.sort()
print(list1)

#2.parametreye göre sıralama
list1.sort(key= lambda x : x[1])
print(list1)


list2 = [{"Name" : "Ali", "Age":25},{"Name" : "Mert", "Age":30},{"Name" : "Tolga", "Age":18}]
list2.sort(key=lambda x : x["Age"])
print(list2)

