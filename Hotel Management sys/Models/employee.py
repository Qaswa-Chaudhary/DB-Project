from config.config import connect_db

class Employee:
    def __init__(self):
        self.conn , self.curr = connect_db()

    def insert_employee(self,emp_name, position, salary,contact_no):
        query = 'insert into Employees(emp_name, position, salary,contact_no) values(%s,%s,%s,%s)'
        self.curr.execute(query,(emp_name, position, salary,contact_no))

        self.conn.commit()
        self.conn.close()

    def get_employee(self,emp_id):
        query = ' select * from Employees where emp_id = %s'
        self.curr.execute(query,(emp_id,))
        return self.curr.fetchall()
    