from views.player import view_player_menu, enough_players, view_create_or_add_player, enter_player, select_actor, \
    view_player_successfully_added, view_player_already_in_tournament, view_sorted_player_by_name, \
    view_sorted_player_by_ranking, view_modify_ranking, missing_players_for_ranking
from models.player import Player
from utils import sort_by_name, sort_by_ranking
from views.utils import print_back_data


def control_player_menu(list_of_actors, in_tournament, list_of_tournaments, tournament=None):
    """
    Cette fonction est appelée depuis soit :
        - 'control_tournament_manager()' auquel cas in_tournament est forcément True et tournament est une instance
        de Tournament. De plus, ce menu est dès lors considéré comme le menu joueurs du tournoi.
        - 'start_program_menu()' auquel cas in_tournament est forcément False et tournament = None. De plus,
        ce menu est désormais considéré comme le menu acteurs (tous les joueurs, y compris ceux n'étant pas inscrits
        au tournoi en cours).

    Cette fonction permet ensuite de gérer les choix de l'utilisateur sur le menu de gestion des joueurs.
    Le menu de gestion des joueurs/acteurs est appelé grâce à la fonction 'view_player_menu()'

    - Si l'utilisateur choisit de quitter le programme (0) tous les acteurs ainsi que le tournoi sont sauvegardés.
    - Si l'utilisateur choisit de retourner au menu précédent (1), la liste des acteurs est retournée s'il s'agit du
    menu acteur, True est retourné s'il s'agit du menu joueurs afin de pouvoir retourner au menu
    control_tournament_manager()
    - Si l'utilisateur choisi l'option 2, s'il s'agit du menu acteurs, un nouveau joueur/acteur est créé grâce à
    l'appel de la fonction 'create_player()', s'il s'agit du menu joueur, il est vérifié que moins de huit joueurs
    sont inscrits au tournoi grâce à l'appel de la fonction 'check_number_of_players()'.
    - Si l'utilisateur choisit de trier les joueurs par nom (3), la fonction 'control_sort_players_by_name' est
    appelée.
    - Si l'utilisateur choisit de trier les joueurs par classement (4), la fonction 'control_sort_players_by_ranking'
    est appelée.
    - Si l'utilisateur choisit de modifier le classement d'un joueur, la fonction 'control_modify_ranking()' est
    appelée.

    Args:
        list_of_actors = la liste de toutes les instances de Joueurs.
        in_tournament = booléen. False = la fonction a été appelée depuis 'start_program_menu()'.
                                 True = la fonction a été appelée depuis 'control_tournament_manager()'
        list_of_tournaments = Liste de toutes les instances de Tournament.
        tournament = None si la fonction a été appelée depuis 'start_program_menu()'
                     une instance de Tournament la fonction a été appelée depuis 'control_tournament_manager()'.

    Returns:
        False = dans le cas où le programme doit être terminé.
        True = permet de revenir au menu précédent 'control_tournament_manager()'
        list_of_actors = permet de revenir au menu précédent 'start_program_menu()' en actualisant la liste des
        acteurs.
    """
    next_menus_access = False
    while not next_menus_access:
        chosen_option = view_player_menu(in_tournament)
        if chosen_option == 0:
            print_back_data()
            Player.back_up_data(list_of_actors)
            if in_tournament:
                tournament.back_up_data(list_of_tournaments)
            return False
        elif chosen_option == 1:
            if not in_tournament:
                return list_of_actors
            else:
                return True
        elif chosen_option == 2:
            if in_tournament:
                list_of_actors = check_number_of_players(list_of_actors, in_tournament, tournament)
            else:
                list_of_actors = create_player(list_of_actors, in_tournament)
        elif chosen_option == 3:
            if in_tournament:
                players_to_sort = tournament.list_of_players
            else:
                players_to_sort = list_of_actors
            control_sort_players_by_name(players_to_sort, in_tournament)
        elif chosen_option == 4:
            if in_tournament:
                players_to_sort = tournament.list_of_players
            else:
                players_to_sort = list_of_actors
            control_sort_players_by_ranking(players_to_sort, in_tournament)
        elif chosen_option == 5:
            if in_tournament:
                list_to_verify = tournament.list_of_players
            else:
                list_to_verify = list_of_actors
            control_modify_ranking(list_to_verify, in_tournament)


def check_number_of_players(list_of_actors, in_tournament, tournament):
    """
    Cette fonction permet list_of_actors = la liste de toutes les instances de Joueurs.de vérifier si moins de huit
    joueurs sont actuellement inscrits au tournoi.
    - Si c'est le cas alors le menu permettent de créer ou ajouter un joueur au tournoi est appelé grâce à la
    fonction 'control_create_or_add_player()'.
    - Si ce n'est pas le cas la fonction 'enough_player()' est appelée.

    Args:
        list_of_actors = la liste de toutes les instances de Joueurs.
        in_tournament = booléen. False = la fonction a été appelée depuis 'start_program_menu()'.
                                 True = la fonction a été appelée depuis 'control_tournament_manager()'
        tournament = None si la fonction a été appelée depuis 'start_program_menu()'
                     une instance de Tournament la fonction a été appelée depuis 'control_tournament_manager()'.

    Returns:
         list_of_actors = la liste de toutes les instances de Joueurs.
    """
    if len(tournament.list_of_players) < 8:
        list_of_actors = control_create_or_add_player(list_of_actors, in_tournament, tournament)
    else:
        enough_players()
    return list_of_actors


def control_create_or_add_player(list_of_actors, in_tournament, tournament):
    """
    Ce menu permet à l'utilisateur de demander à l'utilisateur grâce à l'appel de la fonction
    'view_create_or_add_player()' de créer un nouveau joueur ou d'ajouter un joueur présent dans la base de données au
    tournoi.
    - si l'utilisateur choisit de créer un nouveau joueur (1), la fonction 'create_player()' est appelée.
    - si l'utilisateur choisit d'ajouter un joueur alors la fonction 'add_player()' est appelée.

    Args:
        list_of_actors = la liste de toutes les instances de Joueurs.
        in_tournament = booléen. False = la fonction a été appelée depuis 'start_program_menu()'.
                                 True = la fonction a été appelée depuis 'control_tournament_manager()'
        tournament = None si la fonction a été appelée depuis 'start_program_menu()'
                     une instance de Tournament la fonction a été appelée depuis 'control_tournament_manager()'.

    Returns:
         list_of_actors = la liste de toutes les instances de Joueurs.
    """
    chosen_option = view_create_or_add_player()
    if chosen_option == 1:
        list_of_actors = create_player(list_of_actors, in_tournament, tournament)
    else:
        list_of_actors = add_player(list_of_actors, tournament)
    return list_of_actors


def create_player(list_of_actors, in_tournament, tournament=None):
    """
    Cette fonction permet de créer une instance de Joueur. Les informations du joueur sont récupérées grâce à
    l'appel de la fonction 'enter_player()'.
    L'instance du joueur est ensuite ajoutée à la liste de tous les joueurs (list_of_actors).
    Si le joueur a été ajouté depuis le menu de gestion du tournoi, alors l'instance de joueur est également ajoutée à
    la liste des joueurs inscrits au tournoi.

    Args:
        list_of_actors = la liste de toutes les instances de Joueurs.
        in_tournament = booléen. False = la fonction a été appelée depuis 'start_program_menu()'.
                                 True = la fonction a été appelée depuis 'control_tournament_manager()'
        tournament = None si la fonction a été appelée depuis 'start_program_menu()'
                     une instance de Tournament la fonction a été appelée depuis 'control_tournament_manager()'.

    Returns:
         list_of_actors = la liste de toutes les instances de Joueurs.
    """
    new_player = enter_player(in_tournament)
    player = Player.create_instance(new_player)
    list_of_actors.append(player)
    player.assign_id(list_of_actors)
    if in_tournament:
        tournament.list_of_players.append(player)
    return list_of_actors


def add_player(list_of_actors, tournament):
    """
    Cette fonction permet à l'utilisateur de sélectionner le joueur qu'il souhaite inscrire au tournoi grâce à
    l'appel de la fonction 'select_actor()'.
    Grâce à l'id du joueur sélectionné, l'instance du joueur correspondant est ajoutée à la liste des joueurs
    inscrits au tournoi.

    Args:
        list_of_actors = la liste de toutes les instances de Joueurs.
        tournament = une instance de Tournament.

    Returns:
         list_of_actors = la liste de toutes les instances de Joueurs.
    """
    serialized_players = [player.serialize() for player in list_of_actors]
    actor_id = select_actor(serialized_players)
    for player in list_of_actors:
        if player.id == actor_id:
            if player in tournament.list_of_players:
                view_player_already_in_tournament()
            else:
                tournament.list_of_players.append(player)
                view_player_successfully_added()
    return list_of_actors


def control_sort_players_by_name(list_of_players, in_tournament):
    """
    Cette fonction permet de faire appel à la fonction de classement des joueurs par nom 'sort_by_name()',
    de sérialiser ces joueurs, puis d'afficher ces joueurs à l'utilisateur grâce à l'appel de la fonction
    'view_sorted_player_by_name()'.

    Args:
        list_of_players = une liste composée d'instances de joueurs.
        in_tournament = booléen.
    """
    sorted_players_by_name = sort_by_name(list_of_players)
    serialized_players = [player.serialize() for player in sorted_players_by_name]
    view_sorted_player_by_name(serialized_players, in_tournament)


def control_sort_players_by_ranking(list_of_players, in_tournament):
    """
    Cette fonction permet de faire appel à la fonction de classement des joueurs par classement 'sort_by_ranking()',
    de sérialiser ces joueurs, puis d'afficher ces joueurs à l'utilisateur grâce à l'appel de la fonction
    'view_sorted_player_by_ranking()'.

    Args:
        list_of_players = une liste composée d'instances de joueurs.
        in_tournament = booléen.
    """
    sorted_players_by_ranking = sort_by_ranking(list_of_players)
    serialized_players = [player.serialize() for player in sorted_players_by_ranking]
    view_sorted_player_by_ranking(serialized_players, in_tournament)


def control_modify_ranking(list_of_players, in_tournament):
    """
    Cette fonction vérifie si au moins un joueur existe dans la liste des joueurs fournie :
    - si la liste de joueurs est vide, un message d'information est prodigué à l'utilisateur grâce à la fonction
    'missing_player_for_ranking()'.
    - si au moins un joueur est présent, les joueurs de la liste sont sérialisés et présentés à l'utilisateur grâce à
    la fonction 'view_modifying_ranking()'. L'attribut du joueur est modifié en conséquence.

    Args:
        list_of_players = une liste composée d'instances de joueurs.
        in_tournament = booléen.
    """
    if list_of_players == []:
        missing_players_for_ranking(in_tournament)
    else:
        serialized_players = [player.serialize() for player in list_of_players]
        modified_player = view_modify_ranking(serialized_players)
        list_of_players[modified_player[0]].modify_ranking(modified_player[1])
