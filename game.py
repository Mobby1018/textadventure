import world
import sys
from player import *
from pathlib import Path
import pickle
from os import system, name
from time import sleep
import enemies
import tiles
def SPrint(pause, string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(pause)

def Intro_Text():
    clear()
    SPrint(.05,"""Day 2,437 of the crusting streak.""")
    sleep(1)
    print()
    SPrint(.05,"""It's significantly harder to move your legs now.
You sit a few inches taller than you used to.""")
    sleep(1)
    print()
    SPrint(.05,"""You frollick towards the toilet... well to the best of your ability.
Your crusting streak is about to add another day.""")
    sleep(1)
    print()
    SPrint(.05,"""You sit down...""")
    sleep(1)
    print()
    SPrint(.05,"""and...""")
    sleep(1)
    print()
    print("BAM!")
    sleep(1)
    SPrint(.05,"""You feel something wet hit you.
You then realize that the toilet you are using...""")
    sleep(1)
    print()
    SPrint(.05,"""IT'S A SKIBIDI BIDET!
Out of pure rage you kill the Bidet with your bare hands.""")
    sleep(1)
    print()
    SPrint(.05,"""You must get your revenge.
Those Skibidis ended your crusting streak.""")
    sleep(1)
    print()
    SPrint(.25,"""They.""")
    sleep(1)
    print()
    SPrint(.25,"""Must.""")
    sleep(1)
    print()
    SPrint(.25,"""Pay.""")
def play(saved_world=None, saved_player=None):
    if saved_world and saved_player:
        world._world = saved_world
        player = saved_player
    else:
        world.load_tiles()
        player = Player()
    clear()
    game_loop(player)

def game_loop(player):
    clear()
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break
        sleep(2)
        clear()
def check_for_save():
    if Path("saved_player.p").is_file() and Path("saved_world.p").is_file():
        saved_world = pickle.load(open("saved_world.p", "rb"))
        saved_player = pickle.load(open("saved_player.p", "rb"))
        save_exists = True
    else:
        save_exists = False
    
    if save_exists:
        valid_input = False
        while not valid_input:
            load = input("Saved game found! Do you want to load the game? Y/N ")
            if load in ['Y','y']:
                play(saved_world, saved_player)
                valid_input = True
            elif load in ['N','n']:
                Intro_Text()
                sleep(3)
                play()
                valid_input = True
            else:
                print("Stupid uhh that's not a choice. Freak.")

    else:
        Intro_Text()
        sleep(3)
        play()
if __name__ == "__main__":
    check_for_save()
