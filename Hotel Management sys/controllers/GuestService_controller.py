from Models.Guest_services import guest_service

class GuestService_controller:
    def __init__(self):
        self.control = guest_service()

    def create_GuestService(self,guest_id, service_id,service_date):
        self.control.insert_GuestServices(guest_id, service_id,service_date)

    
    def get_GuestService(self):
        return self.control.get_GuestServices()







