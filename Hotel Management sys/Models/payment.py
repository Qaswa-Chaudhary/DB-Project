from config.config import connect_db

class Payment:
    def __init__(self):
        self.conn, self.curr = connect_db()

    def insert_payment(self,booking_id,payment_date, amount, payment_method):
        query = 'insert into Payments(booking_id,payment_date, amount, payment_method) values(%s,%s,%s,%s)'
        self.curr.execute(query,(booking_id,payment_date, amount, payment_method))

        self.conn.commit()
        self.conn.close()

    def get_payment(self, payment_id):
        query = 'select * from Payments where payment_id = %s'
        self.curr.execute(query,(payment_id,))
        return self.curr.fetchall()