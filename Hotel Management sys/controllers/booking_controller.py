from Models.booking import booking

class booking_controller:
    def __init__(self):
        self.control = booking()

    def create_booking(self,guest_id,room_id,check_in, check_out,booking_date):
        self.control.insert_booking(guest_id,room_id,check_in, check_out,booking_date)

    def get_booking(self,booking_id):
        return self.control.get_booking(booking_id)
