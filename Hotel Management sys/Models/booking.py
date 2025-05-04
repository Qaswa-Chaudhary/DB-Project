from config.config import connect_db

class booking:
    def __init__(self):
        self.conn , self.curr = connect_db()

    def insert_booking(self,guest_id,room_id,check_in, check_out,booking_date):
        query = 'insert into Booking(guest_id,room_id,check_in, check_out,booking_date)'
        self.curr.execute(query(guest_id,room_id,check_in, check_out,booking_date))

        self.conn.commit()
        self.conn.close()

    def get_booking(self,booking_id):
        query = 'select * froom Booking where booking_id = %s'
        self.curr.execute(query,(booking_id,))
        self.curr.fetchall()