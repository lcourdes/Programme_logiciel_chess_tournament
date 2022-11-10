from controller.start_program import *
from models.player import Player

if __name__ == '__main__':
    list_of_actors = Player.load_list_of_actors()
    running_program = True
    while running_program:
        running_program = start_program_menu(list_of_actors)
