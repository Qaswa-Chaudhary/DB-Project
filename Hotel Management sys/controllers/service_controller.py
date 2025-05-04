from Models.service import Service

class service_controller:
    def __init__(self):
        self.control = Service()

    def insert_service(self,service_name,service_cost):
        self.control.insert_service(service_name,service_cost)

    def get_service(self,service_id):
        return self.control.get_services(service_id)