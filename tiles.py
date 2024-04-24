import items, enemies, actions, world
from player import Player

player = Player()
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
        Hmm looks like this is where you started.
        """

    def modify_player(self, the_player):
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        self.looted = False
        super().__init__(x, y)

    def add_loot(self, the_player):
        the_player.inventory.append(self.item)
        self.looted = True

    def modify_player(self, the_player):
        if not self.looted:
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
class FirstBossToiletRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.FirstBossToilet()) 
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
        else:
            return """
            The remnents of a Skibidi Boss can be seen.
            """
class SecondBossToiletRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.SecondBossToilet())
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            *BOOM*
            *BOOM*
            *BOOM*
            *CRASH*
            ANOTHER BOSS TOILET ROOM!!!!
            """
        else:
            return """
            the remnents of a Skibidi Boss can be seen.
            """
class ThirdBossToiletRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.ThirdBossToilet())
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            *BOOM*
            *BOOM*
            *BOOM*
            *CRASH*
            IS THIS THE FINAL BOSS?!?!?!
            """
        else:
            return """
            The remnants of the Final SKibidi boss can be seen.
            Is that a light ahead?
            """

class FindCardboardTubeRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.CardboardTube())

    def intro_text(self):
        if not self.looted:
            return """
            You found a Cardboard Tube (y'know the thing from the toilet paper roll)!
            """
        else:
            return """
            The room is now empty.
            """
class FindToiletSeatRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.ToiletSeat())

    def intro_text(self):
        if not self.looted:
            return """
            You found a Toilet Seat!
            """
        else:
            return """
            The room is now empty.
            """
class FindToiletBrushRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.ToiletBrush())

    def intro_text(self):
        if not self.looted:
            return """
            You found a Toilet Brush!
            """
        else:
            return """
            The room is now empty.
            """
class FindPlungerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Plunger())

    def intro_text(self):
        if not self.looted:
            return """
            You found a Plunger!
            """
        else:
            return """
            The room is now empty.
            """
class LeaveSkibidi(MapTile):
    def intro_text(self):
        return """ """
    def modify_player(self, player):
        if player.boss_defeated == 3:
            print("""
            It appears you have beaten all the bosses.
            """)
            player.victory = True
        else:
            print("There might be a boss or two out there somewhere.")
            return
