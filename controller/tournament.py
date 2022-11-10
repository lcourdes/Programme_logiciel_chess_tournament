from views.tournament import create_load_menu, data_loaded_successfully, no_existing_tournament, enter_tournament, \
    view_tournament_manager_menu, missing_players, main_tournament_menu, view_tournament_details, \
    view_tournament_is_ended, view_round_details, view_round_is_ended, view_get_result_of_match
from views.utils import print_back_data, clear
from models.tournament import Tournament
from models.player import Player
from controller.player import control_player_menu
from controller.myexceptions import NoExistingTournament


def control_create_load_tournament_menu(list_of_actors):
    """
    Cette fonction est appelée depuis 'start_program_menu()'.
    Elle permet de gérer les choix de l'utilisateur sur le menu de création ou de chargement d'un tournoi.
    Le menu de création/chargement d'un tournoi est appelé grâce à la fonction 'create_load_menu()'

    Si l'utilisateur choisi d'accéder à la création d'un tournoi (1), le fonction 'create_tournament()' est appelée.
    Si l'utilisateur choisi de charger un tournoi en cours (else), il est vérifié qu'il est possible de charger un
    tournoi (ie. un tournoi est présent dans la table 'tournament' TinyDB). Si un tournoi existe, une instance de
    Tournament est créée. Si aucun tournoi n'existe, la fonction 'no_existing_tournament()' est appelée.

    Arg:
        list_of_actors: la liste de toutes les instances de Joueurs.

    Returns:
         Cette fonction retourne le retour de la fonction 'control_tournament_manager' qui est donc appelée par ce
         biais.
    """
    tournament = None
    next_menus_access = False
    while not next_menus_access:
        chosen_option = create_load_menu()
        if chosen_option == 1:
            tournament = create_tournament()
            return control_tournament_manager(list_of_actors, tournament)
        else:
            try:
                tournoi_dict = Tournament.load_tournament()
                tournament = Tournament.create_instance(tournoi_dict, list_of_actors)
                data_loaded_successfully(tournament.name)
                return control_tournament_manager(list_of_actors, tournament)
            except NoExistingTournament:
                no_existing_tournament()
                continue


def create_tournament():
    """
    Cette fonction permet de demander à l'utilisateur d'entrer les informations pour créer un tournoi (via l'appel
    de la fonction 'enter_tournament()'.
    Grâce au dictionnaire reçu, il est désormais possible de créer une instance de Tournament.

    Returns:
         tournament = une instance de Tournament.
    """
    new_tournament = enter_tournament()
    tournament = Tournament(new_tournament['name'],
                            new_tournament['place'],
                            new_tournament['date_of_tournament'],
                            new_tournament['description'],
                            new_tournament['game_type'],
                            new_tournament['number_of_rounds'])
    return tournament


def control_tournament_manager(list_of_actors, tournament):
    """
    Cette fonction est appelée depuis 'control_create_load_tournament_menu()'.
    Elle permet de gérer les choix de l'utilisateur sur le menu de gestion d'un tournoi en cours.
    Le menu de gestion d'un tournoi est appelé grâce à la fonction 'view_tournament_manager_menu()'

    Si l'utilisateur choisi de quitter le programme (0) tous les joueurs ainsi que le tournoi sont sauvegardés.
    Si l'utilisateur choisi de revenir au menu principal (1) le tournoi est sauvegardé.
    Si l'utilisateur choisi de gérer les joueurs du tournoi (2), la fonction 'control_player_menu()' est appelée.
    Si l'utilisateur choisi de gérer le tournoi en lui_même (else), il est débord vérifié que huit joueurs sont
    inscrits au tournoi avant d'appeler la fonction 'control_tournament_menu()'.

    Arg:
        list_of_actors = la liste de toutes les instances de Joueurs.
        tournament = une instance de Tournament.

    Returns:
        False : dans le cas où le programme doit être terminé.
        True : permet de revenir au menu précédent 'start_program_menu()'
    """
    next_menus_access = False
    while not next_menus_access:
        chosen_option = view_tournament_manager_menu()
        if chosen_option == 0:
            print_back_data()
            Player.back_up_data(list_of_actors)
            tournament.back_up_data()
            return False
        elif chosen_option == 1:
            tournament.back_up_data()
            return True
        elif chosen_option == 2:
            in_tournament = True
            player_menu = control_player_menu(list_of_actors, in_tournament, tournament)
            if player_menu is False:
                return False
        else:
            if len(tournament.list_of_players) < 8:
                missing_players(len(tournament.list_of_players))
            else:
                running_program = control_tournament_menu(tournament, list_of_actors)
                if not running_program:
                    return False


def control_tournament_menu(tournament, list_of_actors):
    """
    Cette fonction est appelée depuis 'control_tournament_manager()'.
    Tout d'abord, la fonction 'control_tournament()' est appelée pour initialiser ou mettre à jour certaines
    variables de tournament.

    Cette fonction permet ensuite de gérer les choix de l'utilisateur sur le menu de tournoi d'un tournoi en cours.
    Le menu de tournoi d'un tournoi en cours est appelé grâce à la fonction 'main_tournament_menu()'

    Si l'utilisateur choisi de quitter le programme (0) tous les joueurs ainsi que le tournoi sont sauvegardés.
    Si l'utilisateur choisi d'afficher les détails du tournoi' (2), la fonction 'control_tournament_details()' est
    appelée.
    Si l'utilisateur choisi de lancer une tournée (else), la fonction 'control_round()' est appelée.

    Arg:
        list_of_actors = la liste de toutes les instances de Joueurs.
        tournament = une instance de Tournament.

    Returns:
        False : dans le cas où le programme doit être terminé.
        True : permet de revenir au menu précédent 'control_tournament_manager()'
    """
    control_tournament(tournament)
    next_menus_access = False
    while not next_menus_access:
        chosen_option = main_tournament_menu()
        if chosen_option == 0:
            print_back_data()
            Player.back_up_data(list_of_actors)
            tournament.back_up_data()
            return False
        elif chosen_option == 1:
            return True
        elif chosen_option == 2:
            control_tournament_details(tournament)
        elif chosen_option == 3:
            running_program = control_round(tournament, list_of_actors)
            if not running_program:
                return False


def control_tournament(tournament):
    """
    Cette fonction permet de vérifier si les rounds du tournoi en cours ont été instanciés grâce à l'appel de la
    fonction 'check_rounds_initilization()'.
    Cette fonction met à jour les scores des joueurs du tournoi.

    Arg:
        tournament = une instance de Tournament.
    """
    check_rounds_initialization(tournament)
    tournament.get_players_score()


def check_rounds_initialization(tournament):
    """
    Cette fonction instancie les rounds du tournoi si ceux-ci ne sont pas encore créés (cas d'un tournoi qui vient
    d'être créé).

    Arg:
        tournament = une instance de Tournament.
    """
    if tournament.list_of_rounds == []:
        tournament.create_rounds()


def control_tournament_details(tournament):
    """
    Cette fonction permet d'une part, de sérialiser l'instance de tournoi ainsi que la liste des joueurs inscrits au
    tournoi et, d'autre part, d'appeler la fonction 'view_tournament_details()' qui permet d'afficher les détails du
    tournoi en cours à l'aide de la sérialisation du tournoi.

    Arg:
        tournament = une instance de Tournament.
    """
    tournament.get_players_score()
    serialized_players = [player.serialize() for player in tournament.list_of_players]
    serialized_tournament = tournament.serialize()
    view_tournament_details(serialized_players, serialized_tournament)


def control_round(tournament, list_of_actors):
    """
    Cette fonction permet de sélectionner un round en cours.
    Soit un round est déjà en cours (vérification à l'aide de la fonction 'check_if_round_in_progress()',
    soit un nouveau round est lancé, et est donc considéré dès lors comme en cours.

    Arg:
        list_of_actors = la liste de toutes les instances de Joueurs.
        tournament = une instance de Tournament.

    Returns:
        retourne le retour de la fonction 'control_round_details()'
    """
    round = check_if_round_in_progress(tournament)
    if round is None:
        if not is_tournament_ended(tournament):
            round = launch_new_round(tournament)
        else:
            view_tournament_is_ended(tournament.name)
            return True
    return control_round_details(tournament, round, list_of_actors)


def check_if_round_in_progress(tournament):
    """
    Cette fonction vérifie si un round est actuellement en cours de la manière suivante :
        - pour chaque round est vérifié si une liste de match existe.
        - si oui, pour chaque match est vérifié si des résultats sont manquants.
        Si cela est le cas le round est donc en cours.

    Arg:
        tournament = une instance de Tournament.

    Return:
         round : une instance de Round de l'instance Tournament qui est en cours. Si aucun round n'est en cours
         alors round == None
    """
    for round in tournament.list_of_rounds:
        if round.list_of_matches != []:
            for result in round.results_of_matches:
                if result == ([], []):
                    return round


def launch_new_round(tournament):
    """
    Cette fonction permet de considérer une instance Round de l'instance Tournament comme un round en cours en
    appairant les joueurs, en créant les matchs pour ces joueurs.

    Arg:
        tournament = une instance de Tournament.

    Return:
         round : une instance de Round de l'instance Tournament qui est en cours.
    """
    for index, round in enumerate(tournament.list_of_rounds):
        number_of_round = index + 1
        if round.list_of_matches == []:
            if number_of_round == 1:
                round.first_round_pairing()
            else:
                all_matches = tournament.get_all_pairing_already_established()
                sorted_player_by_score = tournament.sort_by_score()
                round.other_round_pairing(sorted_player_by_score, all_matches)
            round.create_matches()
            return round


def control_round_details(tournament, round, list_of_actors):
    """
    Cette fonction permet à l'utilisateur de gérer un round en cours.
    Cette fonction est appelée depuis 'control_round_details()'.
    Cette fonction permet ensuite de gérer les choix de l'utilisateur sur le menu de round en cours appelé grâce à
    la fonction 'view_round_details()'.

    Si l'utilisateur choisit de quitter le programme (0) tous les joueurs ainsi que le tournoi sont sauvegardés.
    Si l'utilisateur choisit d'afficher les détails du tournoi' (2), la fonction 'control_tournament_details()' est
    appelée.
    Si l'utilisateur choisit de rentrer les résultats d'un match (else), la fonction 'control_result_of_match()' est
    appelée. Il est alors vérifié si le round en cours est terminé à l'aide de la fonction 'is_round_ended()',
    si cela est le cas, un message d'information est délivré à l'utilisateur à l'aide de la fonction
    'view_is_round_ended()'.

    Args:
        tournament = une instance de Tournament.
        round = instance de Round considérée comme en cours.
        list_of_actors = la liste de toutes les instances de Joueurs.

    Returns:
        False = dans le cas où le programme doit être terminé.
        True = permet de revenir au menu précédent 'control_tournament_menu()'
    """
    next_menus_access = False
    while not next_menus_access:
        serialized_players = [player.serialize() for player in round.list_of_players]
        serialized_round = round.serialize()
        chosen_option = view_round_details(serialized_players, serialized_round)
        if chosen_option == 0:
            print_back_data()
            Player.back_up_data(list_of_actors)
            tournament.back_up_data()
            return False
        elif chosen_option == 1:
            clear()
            return True
        elif chosen_option == 2:
            control_result_of_match(round, serialized_players, serialized_round)
            if is_round_ended(round):
                view_round_is_ended()
                return True


def control_result_of_match(round, serialized_players, serialized_round):
    """
    Cette fonction permet de gérer les résultats d'un match.
    Les résultats sont d'abord récupérés depuis les informations renseignées par l'utilisateur avec l'appel de la
    fonction 'view_get_result_of_match()'. Ensuite les résultats sont enregistrés dans les instances de Match du round
    en cours.

    Args:
        round = instance de Round considérée comme en cours.
        serialized_players = liste de dictionnaires correspondant à la serialisation des joueurs du tournoi.
        serialized_round = dictionnaire correspondant à la serialisation du round en cours.
    """
    result = view_get_result_of_match(serialized_players, serialized_round)
    match_index = result['match_index']
    player_id = result['player_id']
    score = result['score']
    round.list_of_matches[match_index].get_result(player_id, score)
    round.get_results()
    clear()


def is_round_ended(round):
    """
    Cette fonction permet de vérifier pour le round en cours, si des résultats ont été enregistrés pour tous les match.

    Arg:
        round = instance de Round considérée comme en cours.
    """
    for match in round.list_of_matches:
        if match.result == ([], []):
            return False
    return True


def is_tournament_ended(tournament):
    """
    Cette fonction permet de vérifier si tous les matchs ont été joués, auquel cas le tournoi est terminé.

    Arg:
        tournament = une instance de Tournament.
    Returns:
        booléen indiquant si un tournoi est terminé (True) ou non (False)
    """
    for count, round in enumerate(tournament.list_of_rounds):
        if round.list_of_matches == []:
            return False
        else:
            if count == len(tournament.list_of_rounds):
                for match_result in round.results_of_matches:
                    if match_result == ([], []):
                        return False
    return True
