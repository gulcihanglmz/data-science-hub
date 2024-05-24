#iteration : bir listenin elemanlarını teker teker ziyaret etme olayı
#iterable : üzerinde adımlama yapılabilen (liste,string,tuple)
#iterator : adımlama işini yapan nesnedir. tüm elemanları geziyor nerde kaldığını unutmuyor

numbers = [1,2,3,4,5]
print(dir(numbers)) #eğer bir objenin içinde __iter__ metodu varsa bu iterable'dır ve döngülerle kullanılabilir


i_numbers = numbers.__iter__()
#or
i_numbers = iter(numbers)

print(type(i_numbers))  #<class 'list_iterator'>
print(dir(i_numbers))   #bir iterator'ı iterator yapan şey __next__ metodudur
                        #__next__ metodu ile iterator bir sonraki elemana geçer

print(i_numbers.__next__())
print(next(i_numbers))
print(next(i_numbers))                     
print(next(i_numbers)) 
print(next(i_numbers)) 


#bir döngü çalıştırdığımız zaman o döngüde kullanılacak nesnenin iter metodu çağrılır
#iter metodu bize bir iterator döndürür. 
#iterater, döngü içerisinde bir hata gelene kadar(eleman oldukça) __next__ metodunu çağırır

while True:
    try :
        number = next(i_numbers) #__next__ metodu iterable ile çalışır
        print(number)
    except StopIteration:
        break
    
#class

class New_Range():
    def __init__(self,start,end) :
        self.start = start
        self.end = end
        
    #bu classın iterable olmasını istiyorsak yani döngülerle 
    # kullanmak istiyorsak bu class içinde __iter__ metodu olmalı
    
    def __iter__(self):  #__iter__ metodu, iterable nesnenin iterator'ünü döndürmek için kullanılır. 
        return self
    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        result = self.start
        self.start += 1
        return result
    
newRange = New_Range(10,20)
for i in newRange:
    print(i)
            
        
        

class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.end:
            self.current += 1
            return self.current - 1
        else:
            raise StopIteration

iterator = MyIterator(0, 5)
for number in iterator:
    print(number)


#Iterable: Üzerinde döngü yapılabilen (iterate) her şeydir. 
# Python'da genellikle listeler, tuple'lar, string'ler gibi veri yapıları iterable'dır. 
# Iterable olabilmesi için __iter__ metoduna sahip olması gerekir ve bu metod bir iterator döndürmelidir.

#Iterator: Iterator, üzerinde döngü yapılabilen bir nesnedir. Iterator olabilmesi için __next__ metoduna 
# sahip olması gerekir. __next__ metodu, bir sonraki öğeyi döndürür ve eğer öğeler biterse 
# StopIteration hatası fırlatır.

#__iter__ metodu, iterable nesnenin iterator'ünü döndürmek için kullanılır. 
