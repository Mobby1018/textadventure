class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

class NormalSkibidiToilet(Enemy):
    def __init__(self):
        super().__init__(name="Skibidi Toilet", hp=12, damage=5)

class SmallSkibidiToilet(Enemy):
    def __init__(self):
        super().__init__(name="Small Skibidi Toilet", hp=10, damage=3)

class BigSkibidiToilet(Enemy):
    def __init__(self):
        super().__init__(name="Big Skibidi Toilet", hp=15, damage=8)

class BioEngineeredToilet(Enemy):
    def __init__(self):
        super().__init__(name="Bio-Engineered Skibidi Toilet", hp=20, damage=12)

class SkibidiUrinal(Enemy):
    def __init__(self):
        super().__init__(name="Skibidi Urinal", hp=12, damage=5)

class SkibidiBathtub(Enemy):
    def __init__(self):
        super().__init__(name="Skibidi Bathtub", hp=12, damage=5)

class BossToilet(Enemy):
    def __init__(self):
        super().__init__(name="Boss Toilet", hp=50, damage=20)

class AbnormalToilet(Enemy):
    def __init__(self):
        super().__init__(name="Abnormal Toilet", hp=25, damage=15)
