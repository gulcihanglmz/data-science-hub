# @property , @setter , @deleter
#pythonda gömülü halde(hazır) bulunan class'lara özgü decoratorlar
# @property = metodlara attribute davranışı katar.
# metodları attribute gibi kullanınca onları attribute gibi değiştiremiyoruz bunun için de :@setter


class person:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        #self.namesurname = name + " " + surname
    
    @property
    def namesurname(self):
        return f"{self.name}  {self.surname}"
    
    @property
    def email(self):
        return f"{self.surname}.{self.name}@company.com"
    
    @namesurname.setter
    def namesurname(self,name):
        name , surname = name.split(" ")
        self.name = name
        self.surname = surname

    @namesurname.deleter
    def namesurname(self):
        self.name = None
        self.surname = None
    
person1 = person("Ali","Uzun")

print(person1.name)
print(person1.surname)
print(person1.namesurname)
print(person1.email)

person1.namesurname = "Ayse Yildiz" #bir metodu attribute gibi değiştirdik
print(person1.namesurname)

