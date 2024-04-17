import items, world

class Shop:
    def __init__(self, name, inv):
        self.inv = [items.SmallHealthPotion(), items.LargeHealthPotion(), items.MysteryPotion()]
        self.location_x, self.location_y = world.starting_position
