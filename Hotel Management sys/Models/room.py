from config.config import connect_db

class rooms:
    def __init__(self):
        self.conn , self.curr = connect_db()

    def insert_room(self,room_type,per_night_price,availability):
        query = 'insert into Rooms(room_type,per_night_price,availability) values(%s,%s,%s)'
        self.curr.execute(query(room_type,per_night_price,availability))

        self.conn.commit()
        self.conn.close()
    

    def get_rooms(self,room_id):
        query = 'select * from Rooms where room_id = %s'
        self.curr.execute(query,(room_id,))
        return self.curr.fetchall()