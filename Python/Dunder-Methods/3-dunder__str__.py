#dunder metodlar (magic) pythondaki özel gömülü metodlardır
#bir class tanımladığımızda onun üzerinde  yapılabilecek işlemleri tanımlıyoruz.
#__str__ ve __repr__ (representation)=bir sınıftan oluşturulan nesnelerin string olarak göstermek için
 
from datetime import date
import datetime

a = "Python"
print(str(a))
print(repr(a))

today = date.today()
print(today)
print(str(today))  #kullanıcıya göstermek istediğimiz veri
print(repr(today)) #geliştiriciler için-yorumlayıcı tarafından okunabilecek gösterimler oluşturur


class worker:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    def __repr__(self):
        return f"Worker: {self.name}, {self.age}"
        
        
worker1 = worker("Batu",28)
print(worker1)    #<__main__.worker object at 0x0000044R0516E888> 
#Since worker 1 is an object we have to write __str__ method to write it as string        

print(repr(worker1))
print(worker1.__repr__)

