#*args, **kwargs
def power(x,y):  #positional arguments ->hepsi tam olarak girilmeli(eşit sayıda)
    return x**y

print(power(3,4))

def person(name,surname="not entered",age=" "):  #keyword argument
    return f"Name: {name}, Surname: {surname}, Age: {age}"

print(person("Ali","Calişkan",26))
print(person("Fatma","Gunduz")) 
print(person("Batu",24)) #Surname:24
print(person("Batu",age=24)) #age=24


# *args = istediğimiz kadar parametre -> tuple
def sum(*args):  
    print(args)
    print(type(args))
    for arg in args:
        print(arg)
    
sum(1,2,3,"Python",True)


def mult(*args):
    result = 1
    for arg in args:
        result *= arg
    #print(result) -> none
    return result
    
print(mult(2,4,6))


# def average(*args):
#     if len(args) == 0:
#         return 0  # Eğer hiç argüman yoksa 0 döndür
#     return sum(args) / len(args)

# print(average(5, 7))  # Çıktı: 6.0
# print(average())      # Çıktı: 0


def greeting(message,*args):
    print(message)
    for arg in args:
        print(arg)
print(greeting("Hello","Python",23,True))  #"Python",23,True  = *args



# **kwargs
def funct(**kwargs):  #dictionary
    print(kwargs) 
funct(Name="Derin",age=34) 


def funct2(mandatory,*args,**kwargs):
    print(mandatory)
    for arg in args:
        print(arg)
    for kwarg in kwargs:  
        print(kwarg)    #keys
    for k,v in kwargs.items():  
        print(k,v)      #keys,values
        
funct2(2,4,5,8, Name="Funda", Age=28)  #2:mandatory , 4,5,8:*args, Name="Funda", Age=28:**kwargs
    

