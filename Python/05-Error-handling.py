try:
    a = 5
    b = 0
    c = a/b
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("Else block is running.(there is no error)")
finally:
    print("Finally block is running")

#raise -> to throw an error
try:
    a = 5
    b = 0
    if b==0:
        raise ZeroDivisionError
    c = a/b
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("Else block is running.(there is no error)")
finally:
    print("Finally block is running")

try:
    a = 5
    b = 5
    c = a/b
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("Else block is running.(there is no error)")
finally:
    print("Finally block is running")

try:
    d = x
except NameError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("Else block is running.(there is no error)")
finally:
    print("Finally block is running")


try:
    name = "Ali"
    print(name[10])
except IndexError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("Else block is running.(there is no error)")
finally:
    print("Finally block is running")
    

    
    