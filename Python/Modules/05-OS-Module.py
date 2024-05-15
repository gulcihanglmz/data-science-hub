import os
from datetime import datetime

#getcwd() = current working directory 
print(os.getcwd())

#change directory
#os.chdir("path")

#list directory
print(os.listdir())    #current directory
print(os.listdir("D:\DataScience\Python\Modules"))  

for folder in os.listdir():
    print(folder)
    
#create folder 
#os.mkdir("newfolder")

#nested folder
#os.makedirs("Folder1/folder2/folder3")

#deleting one directory (only empty directory)
#os.rmdir("newfolder")

#deleting nested directory (only empty directory)
#os.removedirs("Folder1/folder2/folder3")

#deleting folder
#os.mkdir("Afolder")

#os.chdir("D:\DataScience\Python\Afolder")
#print(os.getcwd())
#deleting = os.listdir()[0]   #index=0
#os.remove(deleting)
#os.rmdir("Afolder")

#os.chdir("D:\DataScience\Python")
#print(os.getcwd())
#os.rmdir("D:\DataScience\Python\Afolder")


#rename 
#print(os.getcwd())
#os.chdir("D:\DataScience\Python\Modules")
#os.rename("OS-Module.py","05-OS-Module.py")

#os.rename("05-OS-Module.py","D:\DataScience\Python\Modules\OS-Modules.py")


#status of any directory
print(os.stat("D:\DataScience\Python\Modules"))
print(os.stat("D:\DataScience\Python\Modules").st_mode) 
time = datetime.fromtimestamp(os.stat("D:\DataScience\Python\Modules").st_mode)  #zaman damgası
print(time) 

print(os.stat("D:\DataScience\Python\Modules").st_size)  #file size in bytes

#file extention
print(os.path.splitext("D:\\DataScience\\Python\\Modules\\01-Modules.py"))
    
'''
os.getcwd()
os.chdir()
os.listdir()
os.mkdir()
os.makedirs()
os.rmdir()   ->>  klasor silme
os.remove()  ->>  Dosya silme
os.removedirs()
os.listdir()[index]  ->> bulunduğum dizin içindeki .. indexli dosya/klasor
os.rename()
os.rename("..." , "path\....")
os.stat()
os.path.join()
os.path.isfile()  ->>is this file exist?
os.path.isdir()   ->>is this directory exist?

'''