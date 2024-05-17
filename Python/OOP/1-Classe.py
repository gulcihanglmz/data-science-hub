class Employees:
    def __init__(self,name_="",surname_="" ,age_ = 0):
        self.name = name_
        self.surname = surname_
        self.age = age_
        #name,surname,age -> attributes
        #class'a baglı fonksiyonlar -> methods
    def show_info(self):
        print(f"Name : {self.name}  Surname : {self.surname}  Age : {self.age}")
        
        
employe1 = Employees("Maria","James",25)
print(employe1.name,employe1.surname,employe1.age)
employe1.show_info()

employe2 = Employees("Ahmet", "Mehmet", 30)
print(employe2.name,employe2.surname,employe2.age)
employe2.show_info()

#alternative writing
Employees.show_info(employe1)
Employees.show_info(employe2)

employe3 = Employees("Ali","A.")
employe3.show_info()        

employe3 = Employees("Ali",age_=20)
employe3.show_info()        

