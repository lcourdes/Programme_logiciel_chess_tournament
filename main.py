from controller.start_program import start_program_menu
from models.player import Player
from models.tournament import Tournament

if __name__ == '__main__':
    list_of_actors = Player.load_list_of_actors()
    list_of_tournaments = Tournament.load_tournament(list_of_actors)
    running_program = True
    while running_program:
        running_program = start_program_menu(list_of_actors, list_of_tournaments)
