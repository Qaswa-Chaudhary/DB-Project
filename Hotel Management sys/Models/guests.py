from config.config import connect_db


class guest:
    def __init__(self):
        self.conn , self.curr = connect_db()

    def insert_guest(self, guest_name , guest_email, phone_no, address):
        query = 'insert into Guests(guest_name , guest_email, phone_no, address) values (%s,%s,%s,%s)'
        self.curr.execute(query,(guest_name , guest_email, phone_no, address))  

        self.conn.commit()
        self.conn.close()

    def get_guests(self,guest_id):
        query = 'select * from Guests where guest_id = %s'
        self.curr.execute(query,(guest_id,))
        return self.curr.fetchall()
        
    
