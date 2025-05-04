from Models.payment import Payment

class payment_controller:
    def __init__(self):
        self.control = Payment()
    
    def create_payment(self,booking_id,payment_date, amount, payment_method):
        self.control.insert_payment(booking_id,payment_date, amount, payment_method)

    def get_payment(self, payment_id):
        return self.control.get_payment(payment_id)