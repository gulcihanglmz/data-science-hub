def funct(x):
    return x**x

t =funct  #fonksiyonlar da bir değişkene atanabilir
print(t)  #<function funct at 0x00000242E18F62A0>

a = funct
print(a(3))

b = funct(4)
print(b)


#return

def selectOperation(operation):
    def summation(*args):
        result = 0
        for i in args:
            result += i
        return result
        
    def mult(*args):
        result = 1
        for i in args:
            result *= i
        return result
    
    def average(*args):
        if len(args) ==0:
            pass
        return sum(args)/len(args)
    
    if operation == "summation":
        return summation  #summation() dersek fonksiyonu çalıştırır ama biz fonk. kendisini geri döndürdük
    elif operation == "mult":  #fonksiyonun kendisi geri döner.(parantez olursa sonucu geri döner)
        return mult
    elif operation == "average":
        return average
    
sum_funct = selectOperation("summation")
print(sum_funct) #<function selectOperation.<locals>.summation at 0x0000075AFF365999>
print(sum_funct(2,5,8))
#or 
print(selectOperation("summation")(2,5,8))

mult_funct = selectOperation("mult")
print(mult_funct(2,4,6))
#or
print(selectOperation("mult")(2,4,6))

avr_funct = selectOperation("average")
print(avr_funct(7,9))
#or
print(selectOperation("average")(7,9))


print("******************************")

def select_author(author):
    def select_book(book):
        return f"{book} : {author}"
    return select_book

print(select_author("Fyodor Dostoevsky")("The Brothers Karamazov"))
print(select_author("Victor Hugo")("Les Misérables"))

#or 

a = select_author("Fyodor Dostoevsky")
print(a("The Brothers Karamazov"))
b = select_author("Victor Hugo")
print(b("Les Misérables"))

