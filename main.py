from src.config.db import connect, create_tables, is_disconnected, disconnect
from src.entities.Enterprise import Enterprise
from src.entities.Employee import Employee
from src.service.EnterpriseService import EnterpriseService
from src.service.EmployeeService import EmployeeService
	
enterprice_service = EnterpriseService()
employee_service = EmployeeService()

def enterprise_creators():
    enterprice_service.create("PSL")
    enterprice_service.create("Globant")
    enterprice_service.create("Platzi")
    enterprice_service.create("Udemyy")

def employee_creators():
    employee_service.create({'username':"vapedraza",'salary':5500000,'enterprise':1})


# MAIN
if __name__ == '__main__':
    connect()
    create_tables([Enterprise, Employee])
    #enterprise_creators()
    #employee_creators()
    enterprise_record = enterprice_service.find_by_name("PSL")
    if(enterprise_record == None):
        print("Doesn't exist")
    else:
        print(enterprise_record.name)
    print(enterprice_service.edit('Udemyy','Udemy'))
    for row in enterprice_service.find_all():
        print(row.name)
    employee_record = employee_service.find_by_id(1)
    if(employee_record == None):
        print("Doesn't exist employee")
    else:
        print(employee_record.username)
    for row in employee_service.find_all():
        print(row.enterprise.name)
    print(is_disconnected())
    disconnect()
    print(is_disconnected())


