import items, world
import random
import pickle
import time
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
class Player():
    def __init__(self):
        self.inventory = [items.Fist()]
        self.hp = 125
        self.location_x, self.location_y = world.starting_position
        self.victory = False
        self.boss_defeated = 0
    def is_alive(self):
        return self.hp > 0

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)


    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i

        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
            if enemy.name == "Boss Toilet":
                self.boss_defeated += 1
                print("It appears your health got restored as well!")
                if self.boss_defeated == 1:
                    self.hp = 125
                    print("First boss down!")
                elif self.boss_defeated == 2:
                    self.hp = 150
                    print("Another boss down! Just one more to go!")
                elif self.boss_defeated == 3:
                    self.hp = 150
                    print("I think that's all the bosses. Maybe it's time to find an exit.")
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def flee(self, tile):
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

    def save_and_exit(self):
        pickle.dump(self, open( "saved_player.p", "wb" ))
        pickle.dump(world._world, open( "saved_world.p", "wb"))
        print("Game saved!")
        time.sleep(1)
        clear()
        exit()
