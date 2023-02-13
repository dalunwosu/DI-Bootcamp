class Door:
    def __init__(self) -> None:
        self.is_opened = False
    def open_door(self):
        self.is_opened = True
        print("The door is now open")
    def close_door(self):
        self.is_opened = False
        print("The door has been closed")
class BlockedDoor(Door):
   def open_door(self):
        print("Error! A blocked door can't be opened")
   def close_door(self):
        print("Error! A blocked door can't be closed")
blocked_door = BlockedDoor()
blocked_door.open_door()
blocked_door.close_door()
