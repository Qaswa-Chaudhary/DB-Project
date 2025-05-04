from Models.room import rooms

class room_controller:
    def __init__(self):
        self.control = rooms()

    def insert_rooms(self,room_type,per_night_price,availability):
        self.control.insert_room(room_type,per_night_price,availability)

    def get_room(self,room_id):
        return self.control.get_rooms(room_id)
    