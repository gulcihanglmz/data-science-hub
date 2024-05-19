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



class manager(worker):
    
    def __init__(self, name, surname, salary, sub_workers=None):
        super().__init__(name, surname, salary)
        if sub_workers==None:
            self.sub_workers = [] #empty list
        else:
            self.sub_workers = sub_workers
    
    def add_worker(self,add_worker):
        if add_worker not in self.sub_workers:  #self.sub_workers = metod içinden class özelliğine erişim
            self.sub_workers.append(add_worker)
        else:
            self.add_worker = add_worker
    
    def delete_worker(self,del_worker):
        if del_worker in self.sub_workers:
            self.sub_workers.remove(del_worker)  
        
    def show_worker(self):
        for sub_worker in self.sub_workers:
            print(sub_worker.show_info())
            
            
developer1 = developer("Asuman","gunduz",45000,"Python",5)
worker1 = worker("Meryem","tunc",40000)
manager1 = manager("Metin","Ali",50000)

manager1.add_worker(worker1)
manager1.add_worker(developer1)
manager1.show_worker() 

print("*************************")

manager1.delete_worker(developer1)
manager1.show_worker()

print("*************************")

manager2 = manager("Feyza","koç",55000,[worker1,developer1])
manager2.show_worker()


print(isinstance(worker1,worker))       #true
print(isinstance(developer1,worker))    #true
print(isinstance(developer1,developer)) #true
print(isinstance(worker1,developer))    #false
print(isinstance(manager1,worker))      #true
print(isinstance(manager1,developer))   #false

print(issubclass(manager,worker))       #true
print(issubclass(developer,worker))     #true

