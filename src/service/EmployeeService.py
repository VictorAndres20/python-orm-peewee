from src.entities.Employee import Employee
from src.repo.EmployeeRepo import EmployeeRepo

class EmployeeService:

    def __init__(self):
        self.repo = EmployeeRepo()

    def create(self, employee_dict):
        employee = Employee(username = employee_dict['username'], salary = employee_dict['salary'], enterprise = employee_dict['enterprise'])
        self.repo.create(employee)

    def find_by_id(self, id):
        try:
            return self.repo.find_by_id(id)
        except:
            return None

    def edit(self, id, username):
        employee = self.find_by_id(id)
        if(employee == None):
            return False
        else:
            employee.username = username
            self.repo.edit(employee)
            return True

    def find_all(self):
        return self.repo.find_all()