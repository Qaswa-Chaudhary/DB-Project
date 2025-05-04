from config.config import connect_db

class guest_service:
    def __init__(self):
        self.conn, self.curr = connect_db()

    def insert_GuestServices(self,guest_id, service_id,service_date):
        query = 'insert into Guest_Services(guest_id, service_id,service_date)'
        self.curr.execute(query,(guest_id, service_id,service_date))

        self.conn.commit()
        self.conn.close()

    def get_GuestServices(self):
        query = 'select * from Guest_Services'
        self.curr.execute(query)
        self.curr.fetchall()