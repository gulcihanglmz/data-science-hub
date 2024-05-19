
def outFunct():
    print("Out Function running")
    def inFunction(): #çalışması için outFunct içinde çalıştırılması gerek
        print("In function running")
    print("Out function terminated")
    inFunction()

outFunct()     


#######
def calculations(x):
    def sqr(a):       #iç fonksiyonlara dışardan ulaşamıyoruz
        return a**2
    def sqrt(a):
        return a**0.5
    def factorial(a):
        result=1
        for i in range(1,a+1):
            result *= i
        return result
    sqr = sqr(x)     #sadece sonucu döndürür yazdırmaz (return içinde en aşağıda yazdırmalıyız)
    sqrt = sqrt(x)   #return edilen değerleri değişkene atayıp yazdırdık
    factorial = factorial(x)
    return f"sqr:{sqr}, sqrt: {sqrt}, factorial: {factorial}"
    
print(calculations(8))


#######
def sum_mult(*args):
    def summition(tuple):
        return sum(tuple)
    def mult(tuple):
        multiplication = 1
        for i in tuple:
            multiplication *= i
        return multiplication
    
    return f"summition: {summition(args)}, multiplication: {mult(args)}"   
    #dış fonksiyonun iç fonksiyonları geri döndürmesi gerek 
    #args parametresi, dış fonksiyondan iç fonksiyonlara veri geçişini sağlar
    
print(sum_mult(1,2,3,4,5) )  



#args parametresi *args ifadesiyle bir tuple olarak toplanır: (1, 2, 3, 4, 5)
#summition iç fonksiyonu args tuple'ını alır ve toplamını döndürür

