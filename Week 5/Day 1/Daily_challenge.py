from operator import truediv


class Door:
    def __init__(self) -> None:
        self.is_opened=True
    
    def open(self):
        self.is_opened = True
        print("Door is opened")
    
    def close(self):
        self.is_opened = False
        print("Door is closed")

class BlockedDoor(Door):
    def __init__(self):
        self.is_opened = False

    def open(self):
        raise Exception("cannot open a blocked door")
 
    def close(self):
        raise Exception("cannot close a blocked door")


door = Door()
door.open()
door.close()
