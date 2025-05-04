from Models.guests import guest

class guest_controller:
    def __init__(self):
        self.control = guest()

    def create_guest(self, guest_name , guest_email, phone_no, address):
        self.control.insert_guest(guest_name , guest_email, phone_no, address)
    
    def get_guest(self,guest_id):
        return self.control.get_guests(guest_id)
