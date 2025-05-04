from config.config import connect_db

class Service:
    def __init__(self):
        self.conn, self.curr = connect_db()

    def insert_service(self,service_name,service_cost):
        query = 'insert into Services(service_name,service_cost) values(%s,%s)'
        self.curr.execute(query,(service_name,service_cost))

        self.conn.commit()
        self.conn.close()

    def get_services(self,service_id):
        query = 'select * from Services where service_id = %s'
        self.curr.execute(query,(service_id,))
        return self.curr.fetchall()