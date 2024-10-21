from fastapi import FastAPI
from pydantic import BaseModel

class Employee(BaseModel):
    employee_id: int
    employee_name: str
    employee_salary: int

app = FastAPI()

employees = []

@app.get("/")
def fun():
    return employees

@app.get("/employee/")
def read_employee():
    return employees

@app.post("/employee/")
def employee_create(new_employee : Employee):
    employees.append(new_employee)
    return new_employee

@app.put("/employee/{employee_id}")
def update_employee(employee_id: int , updated_employee: Employee):
    for index, employee in enumerate(employees):
        if employee.employee_id == employee_id:
            employees[index] = updated_employee
            return updated_employee
    return {"Error" : "Employee not found"}

@app.delete("/employee/{employee_id}")
def delete_employee(employee_id : int):
    for index , employee in enumerate(employees):
        if employee.employee_id == employee_id:
            del employees[index]
            return {"Message" : "Employee deleted!"}
    return  {"Error" : "Employee not found!"}



'''
Pydantic model, bir veri yapısının nasıl olması gerektiğini tanımlamanı sağlar. Örneğin, 
bir API'ye gönderilen bir JSON verisini Python'daki bir sınıfa dönüştürüp, bu verinin doğru 
formatta olup olmadığını kontrol eder. veya bir verinin modele uygun olduğun için kabul edilmesi
(int , str vs)

FastAPI ve Pydantic birlikte çalışarak, API'ye gelen verileri belirli kurallar çerçevesinde doğrular.
Pydantic sayesinde API'ye gelen hatalı veriler engellenir ve bu da uygulamanın daha güvenli olmasını sağlar.
'''

