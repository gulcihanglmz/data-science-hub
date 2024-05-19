def greeting():
    print("Hello")   
greeting()

def greeting(name):
    print("Hello " + name)   
greeting("Batu")


def convertUpper(text):
    text = text.upper()
    print(text)
convertUpper("hElLo")

#optional parameter (default)
def greeting(name = "anonymous"):
    print("Hello " + name)   
greeting("Batu")
greeting()


def discount(price,percent = 15):
    discount = price * (percent/100)
    newPrice = price-discount
    print(f"Discounted price : {newPrice}")
discount(159,18)
discount(199)


#return fonction

def sum(x,y):    #print
    print(x+y)
sum(5,8)

def sum(x,y):    #None(We cannot assign it to another value without using return.)
    print(x+y)
result = sum(5,8)
print(result)  

def sum(x,y):    #retun (we should print it so it does not print anything, only return)
    return (x+y)
sum(5,8)

def sum(x,y):    #retun 
    return (x+y)
result = sum(5,8)
print(result)


def returnUpperCase(text):
    result = text.upper()
    return result
result =  returnUpperCase("comPuTer eNgiNeer")
print(result)

