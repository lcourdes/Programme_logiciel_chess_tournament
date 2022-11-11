from views.utils import check_input, clear, please_continue, check_date


def create_load_menu():
    """
    Cette fonction permet à l'utilisateur de choisir entre créer un nouveau tournoi ou charger un tournoi en cours.

    Returns:
        chosen_option = integer correspondant à l'une des options proposées.
    """
    print("Menu de création/chargement d'un tournoi.\n")
    print("Veuillez sélectionner une option ci-dessous en spécifiant le chiffre correspondant.\n")
    print("1 - Créer un nouveau tournoi.")
    print("2 - Charger un tournoi en cours.")
    user_input = input()
    chosen_option = check_input(user_input, ["1", "2"])
    clear()
    return chosen_option


def enter_tournament():
    """
    Cette fonction permet à l'utilisateur de rentrer les informations pour créer un tournoi.

    Returns:
         created_tournament = un dictionnaire contenant les informations d'un tournoi.
    """
    print("Pour créer un nouveau tournoi, veuillez remplir les informations ci-dessous.\n")
    print("Entrez le nom du tournoi :")
    name = input()
    print("Entrez le nom du lieu où se déroulera le tournoi :")
    place = input()

    print("Quand débutera le tournoi ?")
    date = input()
    start_date_of_tournament = check_date(date)

    print("Quand se terminera le tournoi ?")
    date = input()
    end_date_of_tournament = check_date(date)

    date_of_tournament = [start_date_of_tournament]
    if end_date_of_tournament != start_date_of_tournament:
        date_of_tournament.append(end_date_of_tournament)

    print("Ajoutez une description :")
    description = input()

    print('Choisissez le type de parties :')
    print("1 - Blitz")
    print("2 - Bullet")
    print("3 - Coup rapide")
    user_input = input()
    chosen_option = check_input(user_input, ["1", "2", "3"])
    game_type = ""
    if chosen_option == 1:
        game_type = "Blitz"
    elif chosen_option == 2:
        game_type = "Bullet"
    elif chosen_option == 3:
        game_type = "Coup rapide"

    print("Par défaut, un tournoi compte 4 tournées.")
    print("Si vous souhaitez modifier le nombre de tournées, veuillez taper ci-dessous le nombre de tournées "
          "souhaité.")
    print("Si le nombre de 4 tournées est correct, taper sur la touche entrée.")
    number_of_rounds = input()

    created_tournament = {'name': name,
                          'place': place,
                          'date_of_tournament': date_of_tournament,
                          'description': description,
                          'game_type': game_type
                          }
    try:
        number_of_rounds = int(number_of_rounds)
        created_tournament['number_of_rounds'] = number_of_rounds
    except ValueError:
        created_tournament['number_of_rounds'] = 4

    print("Le tournoi " + name + " a bien été créé.")
    please_continue()
    return created_tournament


def data_loaded_successfully(name_of_tournament):
    """
    Cette fonction permet d'informer l'utilisateur qu'un tournoi a été trouvé et donc chargé.
    Arg:
        name_of_tournament: string correspond au nom du tournoi qui a été chargé.
    """
    print("Le tournoi " + name_of_tournament + " a bien été chargé.")
    please_continue()


def no_existing_tournament():
    """
    Cette fonction permet d'informer l'utilisateur qu'aucun tournoi ne peut être chargé.
    """
    print("Aucun tournoi n'est enregistré, veuillez créer un nouveau tournoi.")
    please_continue()


def view_tournament_manager_menu():
    """
    Cette fonction permet à l'utilisateur de gérer un tournoi en cours.
    L'utilisateur peut :
        - quitter le programme
        - revenir au menu principal (menu d'accueil)
        - gérer les joueurs du tournoi.
        - gérer le tournoi en lui-même.

    Returns:
        chosen_option = integer correspondant à l'une des options proposées.
    """
    print("Bienvenue dans le menu de gestion du tournoi en cours.\n")
    print("Veuillez sélectionner une option ci-dessous en spécifiant le chiffre correspondant.\n")
    print("0 - Quitter le programme.")
    print("1 - Revenir au menu principal.")
    print("2 - Voir/gérer les joueurs du tournoi en cours.")
    print("3 - Voir/gérer le tournoi en cours.")
    user_input = input()
    chosen_option = check_input(user_input, ["0", "1", "2", "3"])
    clear()
    return chosen_option


def missing_players(n_of_players):
    """
    Cette fonction permet d'informer l'utilisateur que huit joueurs doivent être inscrits pour démarrer le tournoi.

    Args :
        n_of_players = int : le nombre de joueurs actuellement dans le tournoi.
    """
    print("Pour accéder à ce menu, 8 joueurs doivent être inscrits.\nActuellement, le tournoi compte "
          + str(n_of_players)
          + " joueur(s).\n")
    please_continue()


def main_tournament_menu():
    """
    Cette fonction permet à l'utilisateur de gérer un tournoi en lui_même.
    L'utilisateur peut :
        - quitter le programme
        - revenir au menu de gestion d'un tournoi
        - afficher les détails du tournoi.
        - lancer un round.

    Returns:
        chosen_option = integer correspondant à l'une des options proposées.
    """
    print("Menu Tournoi.\n")
    print("Veuillez sélectionner une option ci-dessous en spécifiant le chiffre correspondant.\n")
    print("0 - Quitter le programme.")
    print("1 - Retourner au menu de gestion du tournoi.")
    print("2 - Afficher les détails du tournoi.")
    print("3 - Lancer une tournée.")
    user_input = input()
    chosen_option = check_input(user_input, ["0", "1", "2", "3"])
    clear()
    return chosen_option


def view_tournament_details(serialized_players, serialized_tournament):
    """
    Cette fonction permet d'afficher :
        - les informations principales du tournoi en cours.
        - les scores du tournoi en cours.
        - l'état des rounds et match en cours.

    Arg:
        serialized_players = liste de dictionnaires des joueurs inscrits au tournoi.
        serialized_tournament = dictionnaire regroupant les informations du tournoi en cours.
    """
    print("Tournoi en cours :\n")
    print("Nom : " + serialized_tournament['name'])
    print("Lieu : " + serialized_tournament['place'])
    print("Date de création : " + serialized_tournament['creation_date'][0] + " à "
                                + serialized_tournament['creation_date'][1])
    if len(serialized_tournament['date_of_tournament']) == 1:
        print("Date du tournoi : " + serialized_tournament['date_of_tournament'][0])
    else:
        print("Date du tournoi : " + serialized_tournament['date_of_tournament'][0] + " - "
                                   + serialized_tournament['date_of_tournament'][1])

    print("Nombre de tournées : " + str(serialized_tournament['number_of_rounds']))
    print("Description : " + serialized_tournament['description'])
    print("Type de jeu : " + serialized_tournament['game_type'] + "\n")
    print("*****************************************************************************************\n")
    print("Score des joueurs :\n")
    for player_id, score in serialized_tournament['players_score'].items():
        print(serialized_players[player_id - 1]['name'] + " " + serialized_players[player_id - 1]['first_name']
              + ": " + str(score) + " points.")
    print("\n*****************************************************************************************\n")
    print("Récapitulatif des tournées : \n")
    for round in serialized_tournament['list_of_rounds']:
        if round['list_of_matches'] == []:
            print("La tournée " + round['name'] + " n'a pas encore été créée.")
        else:
            print(round['name'] + " :")
            for match in round['list_of_matches']:
                player_1 = serialized_players[match['list_of_two_players'][0]-1]
                player_2 = serialized_players[match['list_of_two_players'][1]-1]
                if match['result'] == ([], []):
                    print('Le match opposant '
                          + player_1['name'] + " " + player_1['first_name'] + " (" + str(player_1['ranking']) + ")"
                          + " contre "
                          + player_2['name'] + " " + player_2['first_name'] + " (" + str(player_2['ranking']) + ")"
                          + " n'a pas encore été joué."
                          )
                else:
                    winner = explicit_winner(match, player_1, player_2)
                    print("Un match a opposé "
                          + player_1['name'] + " " + player_1['first_name'] + " (" + str(player_1['ranking']) + ")"
                          + " qui a joué les " + match['color_distribution'][match['list_of_two_players'][0]]
                          + " contre "
                          + player_2['name'] + " " + player_2['first_name'] + " (" + str(player_2['ranking']) + "). "
                          + winner)
            print("")
    please_continue()


def explicit_winner(match, player_1, player_2):
    """
    Cette fonction permet d'afficher pour un match les résultats de chacun des deux joueurs du match.

    Arg:
        match = dictionnaire correspondant à la serialisation d'un match.
        player_1 et player_2 = dictionnaire correspondant à la serialisation des deux joueurs de la liste des deux
        joueurs du match.

    Returns:
         winner = une string explicitant qui a gagné le match.
    """
    if match['result'][0][1] == 1:
        winner = "Résultat : " + player_1['name'] + " " + player_1['first_name'] + " a gagné."
    elif match['result'][0][1] == 0:
        winner = "Résultat : " + player_2['name'] + " " + player_2['first_name'] + " a gagné."
    else:
        winner = "Résultat : Pat."
    return winner


def view_round_details(serialized_players, serialized_round):
    """
    Cette fonction permet d'afficher l'état du round en cours (pour chaque match : appairement des joueurs et
    distribution des couleurs).

    Ensuite, l'utilisateur à le choix suivant :
        - quitter le programme,
        - revenir au menu de tournoi en cours,
        - entrer le résultat d'un match.

    Arg:
        serialized_players = liste de dictionnaires correspondant à la serialisation des joueurs du tournoi.
        serialized_round = dictionnaire correspondant à la serialisation du round en cours.

    Returns:
        chosen_option = integer correspondant à l'une des options proposées.
    """
    print("Tournée en cours : " + serialized_round['name'] + "\n")
    for count, match in enumerate(serialized_round['list_of_matches']):
        player_1 = serialized_players[match['list_of_two_players'][0] - 1]
        player_2 = serialized_players[match['list_of_two_players'][1] - 1]
        count += 1
        is_played = ""
        if match['result'] != ([], []):
            is_played = " Match terminé."
        print("Match " + str(count) + " - "
              + player_1['name'] + " " + player_1['first_name'] + " (" + str(player_1['ranking']) + ")"
              + " --- " + match['color_distribution'][match['list_of_two_players'][0]]
              + " vs "
              + player_2['name'] + " " + player_2['first_name'] + " (" + str(player_2['ranking']) + ")"
              + " --- " + match['color_distribution'][match['list_of_two_players'][1]]
              + is_played)
    print("\nVeuillez sélectionner une option ci-dessous en spécifiant le chiffre correspondant.\n")
    print("0 - Quitter le programme.")
    print("1 - Retourner au menu Tournoi.")
    print("2 - Entrer le résultat d'un match.")
    user_input = input()
    chosen_option = check_input(user_input, ["0", "1", "2"])
    return chosen_option


def view_get_result_of_match(serialized_players, serialized_round):
    """
    Cette fonction permet à l'utilisateur de rentrer les résultats d'un match. En premier lieu, l'utilisateur doit
    désigner le match pour lequel il souhaite entrer un résultat. Enfin, l'utilisateur doit choisir entre trois
    options : le premier joueur a gagné, le second joueur à gagné, le match est pat.

    Arg:
        serialized_players = liste de dictionnaires correspondant à la serialisation des joueurs du tournoi.
        serialized_round = dictionnaire correspondant à la serialisation du round en cours.

    Returns:
        results = un dictionnaire {'player_id': ID d'un joueur du match, 'score': 1, 0 ou 0.5}
    """
    print("Pour quel match souhaitez-vous entrer un résultat ? (Entrez le numéro du match)")
    match_number = input()
    correct_input = False
    while not correct_input:
        list_of_valid_choices = ["1", "2", "3", "4"]
        if match_number in list_of_valid_choices:
            match = serialized_round['list_of_matches'][int(match_number) - 1]
            if match['result'] == ([], []):
                correct_input = True
            else:
                print("Ce match a déjà été joué, sélectionnez un autre match.")
                match_number = input()
        else:
            print("Entrez le chiffre 1, 2, 3 ou 4.")
            match_number = input()
    print("\nVeuillez sélectionner une option ci-dessous en spécifiant le chiffre correspondant.\n")

    player_1 = serialized_players[match['list_of_two_players'][0] - 1]
    player_2 = serialized_players[match['list_of_two_players'][1] - 1]
    print("1 - " + player_1['name'] + " " + player_1['first_name'] + " (" + str(player_1['ranking']) + ") a gagné.")
    print("2 - " + player_2['name'] + " " + player_2['first_name'] + " (" + str(player_2['ranking']) + ") a gagné.")
    print("3 - Pat.")
    chosen_option = input()
    correct_input = False
    while not correct_input:
        list_of_valid_choices = ["1", "2", "3"]
        if chosen_option in list_of_valid_choices:
            correct_input = True
        else:
            print("Entrez le chiffre 1, 2 ou 3.")
            chosen_option = input()
    result = {'match_index': int(match_number) - 1}
    player_1_id = serialized_players.index(player_1) + 1
    result['player_id'] = player_1_id
    if chosen_option == "1":
        result['score'] = 1
    elif chosen_option == "2":
        result['score'] = 0
    elif chosen_option == "3":
        result['score'] = 0.5
    return result


def view_round_is_ended():
    """
    Cette fonction permet d'informer l'utilisateur que le round est actuellement terminé.
    """
    clear()
    print("Le round est terminé !")
    please_continue()


def view_tournament_is_ended(tournament_name):
    """
    Cette fonction permet d'informer l'utilisateur que le tournoi est terminé lorsqu'il souhaite lancer une nouvelle
    tournée.
    """
    clear()
    print("Le tournoi " + tournament_name + " est terminé !")
    please_continue()
