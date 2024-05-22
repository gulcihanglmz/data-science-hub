#local , enclosing , global, built-in variables

x = "global x"

def outer():
    x = "enclosing x"
    print(x)
    def inner():
        x= "local x"
        print(x)
    inner()
    
outer()
print(x)

print("**********************")

x = "global x"

def outer():
    x = "enclosing x"
    print(x)
    def inner():
        #x= "local x"
        print(x)
    inner()
    
outer()
print(x)

print("*****************************")

x = "global x"

def outer():
    #x = "enclosing x"
    print(x)
    def inner():
        x= "local x"
        print(x)
    inner()
    
outer()
print(x)

print("***********************")


x = "global x"

def funct():
    global x
    x = 5
    
funct()
print(x)

