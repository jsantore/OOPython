from __future__ import annotations
import string
class Room:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_rug_size(self):
        return self.width* self.height
    def add_name(self, roomName:string):
        # this is not recommended for 'enterprise code'
        # It is legal, but now some objects have an extra
        #instance variable
        self.roomName = roomName
    def __add__(self, other:Room)->int:
       return self.get_rug_size()+other.get_rug_size()

