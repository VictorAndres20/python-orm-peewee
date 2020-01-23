from src.entities.Employee import Employee

class EmployeeRepo:

    def create(self, employee):
        return Employee.create(username=employee.username, salary=employee.salary, enterprise=employee.enterprise)

    def find_by_id(self, id):
        return Employee.get(id=id)

    def find_by_salary(self, salary):
        return Employee.select().where(Employee.salary == salary)

    def edit(self, employee):
        employee.save()
    
    def find_all(self):
        return Employee.select().order_by(Employee.username.asc())