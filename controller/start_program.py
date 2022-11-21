from views.start_program import view_start_program
from views.utils import print_back_data
from controller.tournament import control_create_load_tournament_menu
from controller.player import control_player_menu
from models.player import Player


def start_program_menu(list_of_actors, list_of_tournaments):
    """
    Cette fonction est appelée uniquement depuis le main.py.
    Elle permet de gérer les choix de l'utilisateur sur le menu d'accueil du programme.
    Le menu d'accueil est appelé grâce à la fonction 'view_start_program()'.
    Si l'utilisateur choisi d'accéder au menu des acteurs, la fonction 'control_player_menu()' est appelée.
    Si l'utilisateur choisi d'accéder au menu de gestion d'un tournoi, la fonction 'control_create_load_tournament(
    )' est appelée.

    Arg:
        list_of_actors: la liste de toutes les instances de Joueurs.
        list_of_tournaments = Liste de toutes les instances de Tournament.

    Returns:
         Etant donnée qu'une boucle while est présente, il est possible à tout moment de retourner à ce menu. Cette
         boucle se termine lorsque la fonction retourne 'False' ce qui met fin au main.py et donc au programme.
    """
    tournament = None
    next_menus_access = False
    while not next_menus_access:
        chosen_option = view_start_program()
        if chosen_option == 0:
            print_back_data()
            Player.back_up_data(list_of_actors)
            if tournament is not None:
                tournament.back_up_data(list_of_tournaments)
            return False
        elif chosen_option == 1:
            in_tournament = False
            list_of_actors = control_player_menu(list_of_actors, in_tournament, list_of_tournaments)
            if list_of_actors is False:
                return False
        elif chosen_option == 2:
            running_program = control_create_load_tournament_menu(list_of_actors, list_of_tournaments)
            if running_program is False:
                return False
