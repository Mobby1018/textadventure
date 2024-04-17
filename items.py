class Item():
    
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return"{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class ToiletPaper(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Toilet Paper",
                         description="{} sheets of toilet paper.".format(str(self.amt)),
                         value=self.amt)

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
                         damage=12)

class Plunger(Weapon):
    def __init__(self):
        super().__init__(name="Plunger",
                         description="What's thought to be the ultimate weapon, it can be used to force the Skibidi Toilets inside their bowl.",
                         value=20,
                         damage=100)

class Potion(Item):
    def __init(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class SmallHealthPotion(Potion):
    def __init__(self):
        super().__init__(name="Small Health Potion",
                         description="A small potion, it seems to be made of toilet water? It has a strange dark color to it.",
                         value=10,
                         damage=15)

class LargeHealthPotion(Potion):
    def __init__(self):
        super().__init__(name="Large Health Potion",
                         description="A large potion, it seems to be made of toilet water? IT has a strange dark color to it, but there is a large \"log\" floating in it.",
                         value=25,
                         damage=40)

class MysteryPotion(Potion):
    def __init__(self):
        super().__init__(name="Mystery Potion",
                         description="This potion has some green swirls within the dark color. I wander what would happen if you drank it?",
                         value=1,
                         damage=100)
