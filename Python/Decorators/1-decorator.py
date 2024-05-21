#decorator'ın kendisi de bir fonksiyondur, var olan fonksiyonlara özellikler ekler(ne kadar süre çaılıştı vs)

def decorator(funct):
    def wrapper():
        print("Started")
        funct()
        print("Terminated")
    return wrapper


@decorator
def say_hello():
    print("Hello!")

say_hello()

#decorator'ler, gerçek fonksiyonlarınızın etrafını saran ve onların
#davranışlarını değiştiren veya genişleten fonksiyonlardır
#mesela elimizde 100 fonksiyon var bu fonksiyonlara özellikleri teker teker eklemek yerine
#decorator olarak tanımlayıp her fonksiyona bu özelllikleri aktarmış oluyoruz
    

#Dekoratör, aldığı parametreleri wrapper fonksiyonuna verir ve bu parametreler, 
#wrapper içinde orijinal fonksiyona iletilir ve çalıştırılır.   


'''
Decorator kullanım alanaları : 
Logging = Bir fonksiyonun ne zaman çalıştığını, hangi argümanlarla çağrıldığını ve ne döndürdüğünü takip etmek 
Authorization = Belirli kullanıcıların belirli işlemleri yapma yetkisi
Caching = Fonksiyon sonuçlarını önbelleğe alarak performansı artırır
Timing = fonksiyonun ne kadar sürede çalıştığını ölçmek 
'''
  
  