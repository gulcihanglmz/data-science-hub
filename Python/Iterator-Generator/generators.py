# generator'lar, iterator'ların özel bir türüdür ve büyük veri setleriyle çalışırken 
# belleği verimli kullanmanın bir yoludur.Generator'lar, büyük veri setlerini bir seferde 
# bir öğe olarak hesaplayıp döndüren fonksiyonlardır. 
# Bu, belleği verimli kullanarak verileri bir seferde bir parça halinde işlemeyi sağlar.

#kısaca generator , bellekte yer işgal etmeyen bir generator üretir.

def cube():
    result = []              #oluşturduğumuz liste bellek üzerinde yer kaplıyor
    for i in range(5):
        result.append(i**3)
    return result

print(cube())

#generator ile yapmak
def cube():
    for i in range(5):
        yield i**3   # oluşturulan değer bir yerde saklanmıyor 2.defa ulaşamıyoruz
    
print(cube())   #<generator object >

for i in cube():
    print(i)
    


generator = (i**3 for i in range(5))  #listelerdeki köşeli parantez yerine normal parantez kullanılır
print(generator)
for i in generator:
    print(i)


#dosya okuma 
def read_file_line_by_line(file_path):
    with open(file_path,"r") as file:
        for line in file:
            yield line.strip()
            
file_path = "Files\\files.txt"

# Generator'ı kullanarak dosyayı satır satır okuma
line_gen = read_file_line_by_line(file_path)
for line in line_gen:
    print(line)
    
