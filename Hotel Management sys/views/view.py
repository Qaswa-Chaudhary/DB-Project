from config.config import connect_db 

class views:
    def __init__(self):
        self.conn, self.curr = connect_db()

    def view_booking_details(self):
        query = 'select * from GuestBookingDetails'
        self.curr.execute(query)
        return self.curr.fetchall()
    
    def view_payment_history(self):
        query = 'select * from PaymentHistory'
        self.curr.execute(query)
        return self.curr.fetchall()
    
    def Service_used(self):
        query = 'select * from UsedService'
        self.curr.execute(query)
        return self.curr.fetchall()
