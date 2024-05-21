def summation(x,y):
    return x+y
def mult(x,y):
    return x*y

def operation(funct,a,b):
    return funct(a,b)

print(operation(summation,5,9))
#summation() -> bu fonksiyonu çalıştır ordan dönen değeri gönder
#summation -> fonksiyonun kendisini gönder

print(operation(mult,5,9))
    
    
list1 = [1,2,3,4,5]
list2 = [1,2,3,8,7,9,10]

def sqr(x):
    return x**2
def cube(x):
    return x**3

def map_funct(funct,list):
    result = []
    for i in list:
        result.append(funct(i))
    return result

print(map_funct(sqr,list1))
print(map_funct(cube,list2))     


print("************************")

def half(x):
    return x/2
def double(x):
    return x*2

def apply_operation(funct,numberList):
    result = []
    for i in numberList:
        result.append(funct(i))
    return result

numbers_list = [10, 20, 30, 40, 50]

print(apply_operation(half,numbers_list))
print(apply_operation(double,numbers_list))

    
    