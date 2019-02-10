from typing import Tuple


class Door:
    def __init__(self, driver, next_level: str = '', entering_pos: Tuple[int, int] = (0, 0)):
        self.driver = driver
        self.next_level = next_level
        self.entering_pos = entering_pos

    def enter_room(self, player):
        from src.platforms.Room import load_room
        from src.platforms.StorageRoom import load_storage_room

        if self.next_level == 'storage':
            self.driver.state.level = load_storage_room(self.driver.state.level.name, self.driver)

        else:
            self.driver.state.level = load_room(self.next_level, self.driver)

        player.char.move_to(*self.entering_pos)
        return
