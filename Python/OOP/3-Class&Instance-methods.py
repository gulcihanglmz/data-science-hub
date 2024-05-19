from datetime import date

class employees:
    raise_rate = 1.1
    employee_number = 0
    
    def __init__(self, name, age):  #__init__ = constructor 
        self.name = name
        self.age = age
        employees.employee_number += 1
    
    # Instance method
    def knowledges(self):
        return f"Name: {self.name}  Age: {self.age}"
    
    # Class method
    @classmethod
    def NumberOfEmployee(cls):
        return f"Number of employee number: {cls.employee_number}" 
    
    # Class method 
    @classmethod 
    def CreateWithString(cls, str_):
        name, age = str_.split("-")
        return cls(name, int(age))  # name-age -> instance of the class
    
    @classmethod
    def CreateWithDateBirth(cls, name, birth):
        return cls(name, (date.today().year - birth))
    
    #cls=bir metodu class ismi ile oluşturarak diğer alt classların da bu metodu kullanmasını sağlar.
    '''
    cls(name, (date.today().year - birth)) ifadesi, cls sınıfını çağırarak yeni bir sınıf örneği (instance) oluşturur. 
    Bu, normalde bir sınıfı çağırarak (MyClass(name, age))
    bir örnek oluşturduğunuz gibi çalışır, ancak burada sınıfın ismi yerine cls kullanılır.
    '''
    
    #bir class'ın bir örneğine veya class'ın kendisine ait olmayan metotları tanımlamak için staticmethod kullanılır. 
    #sınıfın bir örneği (self) veya sınıfın kendisi (cls) üzerinde işlem yapamaz
    #static method
    @staticmethod
    def calculate_birthDate(employee):
        return date.today().year - employee.age
        

# Create employees
employee1 = employees("Ali", 25)
print(employee1.knowledges())

employee2 = employees.CreateWithString("Cemre-32")
print(employee2.knowledges())

employee3 = employees.CreateWithDateBirth("Elif", 1990)
print(employee3.knowledges())

print(employees.employee_number)

# Create an employee with CreateWithString method
employee4 = employees.CreateWithString("Obje-78")
print(employee4.knowledges())


