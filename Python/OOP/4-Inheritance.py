class worker:
    raise_rate = 1.1
    def __init__(self,name,surname,salary):
        self.name=name
        self.surname=surname
        self.salary=salary
        self.email= surname+name+"@company.com"
        
    def show_info(self):
        return ("Name: {} ,Surname: {}, Salary: {}, Email: {}"
                .format(self.name,self.surname,self.salary,self.email))
    
class developer(worker):
    def __init__(self, name, surname, salary,language,experience):
        super().__init__(name, surname, salary)
        self.language = language
        self.experience = experience
        
    def experienceYear(self):
        return f"Experience: {self.experience} year"
    
    raise_rate = 1.3
    #override 
    def show_info(self):
        return ("Name: {} ,Surname: {}, Salary: {}, Email: {}, Language: {}"
                .format(self.name,self.surname,self.salary,self.email,self.language))

        
developer1 = developer("Asuman","gunduz",45000,"Python",5)
worker1 = worker("Meryem","tunc",40000)

print(worker1.show_info())
print(developer1.show_info())

print(worker1.raise_rate)
print(developer1.raise_rate)

print(developer1.experienceYear())

        