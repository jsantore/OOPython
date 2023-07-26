from ComputerInstallation import ComputerInstallation
from Room import Room

class ComputerRoom(Room, ComputerInstallation):
    def __init__(self):
        super().__init__(20, 20)

    def can_add_computer(self)->bool:
        # if there is more than 8 square feet/computer
        # then there is room for another computer
        floor_space = self.get_rug_size()
        current_comp_count = len(self.computers)
        return floor_space/current_comp_count > 8