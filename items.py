class Item():
    
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return"{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Fist(Weapon):
    def __init__(self):
        super().__init__(name="Fist",
                         description="Literally just your fist.",
                         value=0,
                         damage=1)
class CardboardTube(Weapon):
    def __init__(self):
        super().__init__(name="Cardboard Tube",
                         description="The cardboard tube from the center of a toilet paper roll.",
                         value=0,
                         damage=5)

class ToiletSeat(Weapon):
    def __init__(self):
        super().__init__(name="Toilet Seat",
                         description="The seat from a toilet you found, probably better than the carboard tube you had.",
                         value=10,
                         damage=10)

class ToiletBrush(Weapon):
    def __init__(self):
        super().__init__(name="Toilet Brush",
                         description="A toilet brush. It's quite old and a little crusty. But is a little more practical than the toilet seat.",
                         value=15,
                         damage=15)

class Plunger(Weapon):
    def __init__(self):
        super().__init__(name="Plunger",
                         description="What's thought to be the ultimate weapon, it can be used to force the Skibidi Toilets inside their bowl.",
                         value=20,
                         damage=50)

