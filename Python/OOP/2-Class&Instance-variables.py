class employees:
    raise_rate = 1.1
    employee_number = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        employees.employee_number += 1
        
employee1 = employees("Ali",40000)
employee2 = employees("Ahmet",35000)

print(employee1.__dict__)
print(employee2.__dict__)

print(employee1.raise_rate)
print(employees.raise_rate)

print(employees.__dict__)

#change raise_rate for all employees
employees.raise_rate = 1.3
print(employee1.raise_rate)
print(employee2.raise_rate)

#change raise_rate for specific employees -> it will be added as self.raise_rate=raise_rate for employee1
employee1.raise_rate = 1.5
print("employee1 raise_rate : ",employee1.raise_rate)


print(employee1.__dict__)
print(employee2.__dict__)

print("Number of employee : " ,employees.employee_number)

