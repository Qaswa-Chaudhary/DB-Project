from Models.employee import Employee

class emp_controller:
    def __init__(self):
        self.control = Employee()

    def insert_employee(self,emp_name, position, salary,contact_no):
        self.control.insert_employee(emp_name, position, salary,contact_no)

    def get_employee(self,emp_id):
        return self.control.get_employee(emp_id)