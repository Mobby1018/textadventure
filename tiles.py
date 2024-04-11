import items, enemies, actions, world

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, the_player):
        raise NotImplementedError()
    
    def adjacent_moves(self):
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves
    
    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.SaveAndExit())
        return moves

class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You snap back into consciousness. You're in a white room. The memories from before come in flashes. 
        You remember sitting on the toilet, excited to add on to the crust. You finish and go to stand up, and BAM!
        The toilet tank lid pops off and hits you in the head. 
        You notice that you can move a little more free than usually. You reach down and realize... 
        YOUR CRUST! IT'S GONE! That toilet... it must be one of those so called "Skibidi Toilets".
        That damn toilet. I bet it cleaned my crust!
        """

    def modify_player(self, the_player):
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, the_player):
        the_player.inventory.append(self.item)

    def modify_player(self, the_player):
        self.add_loot(the_player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

class EmptyPath(MapTile):
    def intro_text(self):
        return """
        A White hallway with nothing to see
        """

    def modify_player(self, the_player):
        pass

class ToiletRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.NormalSkibidiToilet())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            You see a Skibidi Toilet in the center of the room.
            """
        else:
            return """
            The shattered corpse of a Skibidi Toilet can be seen in the center of the room.
            """
class SmallToiletRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.SmallSkibidiToilet())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            You see a smaller than usual Skibidi Toilet in the center of the room.
            """
        else:
            return """
            The shattered corpse of a Skibidi Toilet can be seen in the center of the room.
            """

class BigToiletRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.BigSkibidiToilet())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            You see a Bigger than usual Skibidi Toilet in the center of the room.
            """
        else:
            return """
            The shattered corpse of a Skibidi Toilet can be seen in the center of the room.
            """

class BioToiletRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.BioEngineeredToilet())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            You see a Bio-Engineered Skibidi Toilet in the center of the room.
            """
        else:
            return """
            The shattered corpse of a Bio-Engineered Skibidi Toilet can be seen in the center of the room.
            """
class UrinalRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.SkibidiUrinal())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            You see a Skibidi Urinal in the center of the room.
            """
        else:
            return """
            The shattered corpse of a Skibidi Urinal can be seen in the center of the room.
            """
class BathRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.SkibidiBathtub())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            You see a Skibidi Bathtub in the center of the room.
            """
        else:
            return """
            The shattered corpse of a Skibidi Bathtub can be seen in the center of the room.
            """
class AbnormalRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.AbnormalToilet())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            You see an Abnormal Skibidi Toilet in the center of the room.
            """
        else:
            return """
            The shattered remains of an Abnormal Skibidi Toilet can be seen in the center of the room.
            """
class BossToiletRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.BossToilet())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            *BOOM*
            *BOOM*
            *BOOM*
            *CRASH*
            A GIANT SKIBIDI TOILET CRASHES THROUGH THE ROOF!
            IS THIS A BOSS???!??!??!?!
            """

class FindTPRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.ToiletPaper(10))

    def intro_text(self):
        return """
        You found some Toilet Paper!
        """
class FindCardboardTubeRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.CardboardTube())

    def intro_text(self):
        return """
        You found a Cardboard Tube (y'know the thing from the toilet paper roll)!
        """
class FindToiletSeatRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.ToiletSeat())

    def intro_text(self):
        return """
        You found a Toilet Seat!
        """
class FindToiletBrushRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.ToiletBrush())

    def intro_text(self):
        return """
        You found a Toilet Brush!
        """
class FindPlungerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Plunger())

    def intro_text(self):
        return """
        You found a Plunger!
        """
class LeaveSkibidi(MapTile):
    def intro_text(self):
        return """
        You have beaten all of the Skibidi's.
        Now you can return to crusting!
        """
    def modify_player(self, player):
        player.victory = True
