
f = open("Files\\files.txt","r")
content = f.read()
print(content)
f.close()

#if you don't want to close the file manually, use "with open() as ..."
with open("Files\\files.txt","r") as f:
    content = f.read()
    print(content)
    
   
#default mode = read()
with open("Files\\files.txt") as f:
    content = f.read()
    print(content)
    
#readlines() -> to create a list
with open ("Files\\files.txt") as f:
    content = f.readlines()
    print(content)


with open("Files\\files.txt") as f:
    content = f.readlines()
    print(content,end="")
    
    
with open("Files\\files.txt","r") as f:
    content = f.read(10)
    print(content,end="")
    content = f.read(10)
    print(content,end="")
    content = f.read(10)
    print(content,end="")
    
with open("Files\\files.txt","r") as f:
    read_amount = 10
    content = f.read(read_amount)
    while len(content) > 0:
        print(content,end="")
        content = f.read(read_amount)

#write 
with open("file2","w") as f:
    f.write("Python")
#append
with open("file2","a") as f:
    f.write("Lessons")

#copy 
with open("Files\\files.txt","r") as readfile:
    with open("file2","w") as writefile:
        for i in readfile:
            writefile.write(i)
            

#copy , read , write png,jpg  ->>  wb , rb  (b=binary mode)
with open("Files\\Python.png","rb") as readfile:
    with open("Files\\Python2.png","wb") as writefile:
        read_amount = 1024
        content = readfile.read(read_amount)
        while len(content) > 0:
            writefile.write(content)
            content = readfile.read(read_amount)

        
