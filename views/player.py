from views.utils import *


def view_player_menu(in_tournament):
    """
    Cette fonction permet à l'utilisateur de gérer les joueurs.
    L'utilisateur peut :
        - quitter le programme
        - revenir au menu précédent (celui-ci dépend de la variable in_tournament)
        - trier les joueurs par nom
        - trier les joueurs par classement
        - modifier le classement d'un joueur.

    Returns:
        chosen_option = integer correspondant à l'une des options proposées.
    """
    if not in_tournament:
        print("Menu de gestion des joueurs de la base de données.\n")
        print("Veuillez sélectionner une option ci-dessous en spécifiant le chiffre correspondant.\n")
        print("0 - Quitter le programme.")
        print("1 - Retourner au menu principal.")
        print("2 - Créer un profil Joueur.")
        print("3 - Trier les joueurs par nom.")
        print("4 - Trier les joueurs par classement.")
        print("5 - Modifier le classement d'un joueur.")
    else:
        print("Menu de gestion des joueurs du tournoi en cours.\n")
        print("Veuillez sélectionner une option ci-dessous en spécifiant le chiffre correspondant.\n")
        print("0 - Quitter le programme.")
        print("1 - Retourner au menu de gestion du tournoi.")
        print("2 - Ajouter un joueur au tournoi en cours.")
        print("3 - Trier les joueurs du tournoi par nom.")
        print("4 - Trier les joueurs du tournoi par classement.")
        print("5 - Modifier le classement d'un joueur du tournoi.")
    user_input = input()
    chosen_option = check_input(user_input, ["0", "1", "2", "3", "4", "5"])
    clear()
    return chosen_option


def enter_player(in_tournament):
    """
    Cette fonction permet à l'utilisateur de rentrer les informations pour créer un nouveau joueur.

    Returns:
         player = un dictionnaire contenant les informations d'un joueur.
    """
    print("Pour créer un joueur, veuillez remplir les informations ci-dessous.\n")
    print("Entrez le nom de famille du joueur :")
    name = input()
    name = name.capitalize()
    print("Entrez le prénom du joueur :")
    first_name = input()
    first_name = first_name.capitalize()

    print("Entrez la date de naissance du joueur :")
    date = input()
    date_of_birth = check_date(date)

    print("Entrez le genre du joueur :")
    gender = input()
    print("Entrez le classement du joueur :")
    ranking = input()
    ranking_is_number = False
    while ranking_is_number is False:
        try:
            ranking = int(ranking)
            if ranking > 0:
                ranking_is_number = True
            else:
                print("Entrez un chiffre positif :")
                ranking = input()
        except ValueError:
            print("Entrez un chiffre :")
            ranking = input()
    if in_tournament:
        print("\nLe joueur a bien été créé et ajouté au tournoi.")
    else:
        print("\nLe joueur a bien été ajouté à la base de données.")
    player = {
        'name': name,
        'first_name': first_name,
        'date_of_birth': date_of_birth,
        'gender': gender,
        'ranking': ranking
    }
    please_continue()
    return player


def enough_players():
    """
    Cette fonction permet d'informer l'utilisateur que le tournoi compte déjà huit joueurs et qu'il est donc
    impossible d'ajouter de joueurs supplémentaires.
    """
    print("Le tournoi compte huit inscrits, celui-ci est complet. Il est donc impossible d'ajouter de nouveaux "
          "joueurs.")
    print("Si vous souhaitez ajouter un nouveau joueur à la base de données, rendez-vous au menu principal puis "
          "'Créer un profil joueur'.")
    please_continue()


def view_create_or_add_player():
    """
    Cette fonction permet à l'utilisateur de choisir entre créer un joueur ou sélectionner un joueur à ajouter eu
    tournoi.

    Returns:
        chosen_option = integer correspondant à l'une des options proposées.
    """
    print("Veuillez sélectionner une option ci-dessous en spécifiant le chiffre correspondant.\n")
    print("1 - Créer un nouveau joueur et l'ajouter au tournoi.")
    print("2 - Sélectionner un joueur de la base et l'ajouter au tournoi.")
    user_input = input()
    chosen_option = check_input(user_input, ["1", "2"])
    clear()
    return chosen_option


def select_actor(serialized_players):
    """
    Cette fonction permet à l'utilisateur de visualiser tous les joueurs de la base de données, et lui permettre
    d'en choisir un.

    Arg:
        serialized_players = liste des dictionnaires correspondant aux informations de chacun des joueurs connus.
    Returns:
        chosen_input = l'id du joueur que l'utilisateur souhaite inscrire au tournoi.
    """
    print("Joueurs inscrits dans la base de données : \n")
    list_of_valid_choices = []
    for count, player in enumerate(serialized_players):
        count += 1
        list_of_valid_choices.append(str(count))
        print(str(count) + " - "
              + player['name'] + " "
              + player['first_name'] + ", "
              + "classement : " + str(player['ranking']) + ", "
              + "date de naissance : " + player['date_of_birth'] + ", "
              + "sexe : " + player['gender']
              )
    print("\nVeuillez sélectionner un joueur en spécifiant le chiffre correspondant.")
    user_input = input()
    chosen_input = check_input(user_input, list_of_valid_choices)
    return chosen_input


def view_player_already_in_tournament():
    """
    Cette fonction permet d'informer l'utilisateur que le joueur sélectionné est déjà inscrit dans le tournoi.
    """
    print("\nCe joueur est déjà inscrit dans le tournoi en cours.")
    please_continue()


def view_player_successfully_added():
    """
    Cette fonction permet d'informer l'utilisateur que le joueur sélectionné a bien été inscrit dans le tournoi.
    """
    print("\nLe joueur a bien été ajouté au tournoi.")
    please_continue()


def view_sorted_player_by_name(sorted_player_by_name, in_tournament):
    """
    Cette fonction permet de visualiser des joueurs classés par nom.

    Args:
        sorted_player_by_name = liste de dictionnaire de joueurs classés par nom.
        in_tournament = booléen.
    """
    if len(sorted_player_by_name) < 2:
        if in_tournament:
            print("Le nombre de joueurs inscrits au tournoi est insuffisant pour montrer un classement.")
        else:
            print("Le nombre de joueurs dans la base de données est insuffisant pour montrer un classement.")
    else:
        for player in sorted_player_by_name:
            print(player['name'] + " "
                  + player['first_name'] + ", "
                  + "classement : " + str(player['ranking']) + ", "
                  + "date de naissance : " + player['date_of_birth'] + ", "
                  + "sexe : " + player['gender']
                  )
    please_continue()


def view_sorted_player_by_ranking(sorted_player_by_ranking, in_tournament):
    """
    Cette fonction permet de visualiser des joueurs classés par classement.

    Args:
        sorted_player_by_ranking = liste de dictionnaire de joueurs classés par classement.
        in_tournament = booléen.
    """
    if len(sorted_player_by_ranking) < 2:
        if in_tournament:
            print("Le nombre de joueurs inscrits au tournoi est insuffisant pour montrer un classement.")
        else:
            print("Le nombre de joueurs dans la base de données est insuffisant pour montrer un classement.")
    else:
        for player in sorted_player_by_ranking:
            print("classement : " + str(player['ranking']) + ", "
                  + player['name'] + " "
                  + player['first_name'] + ", "
                  + "date de naissance : " + player['date_of_birth'] + ", "
                  + "sexe : " + player['gender']
                  )
    please_continue()


def missing_players_for_ranking(in_tournament):
    """
    Cette fonction permet d'informer l'utilisateur que pour modifier le classement d'un joueur, au moins un joueur
    doit déjà avoir été créé.
    """
    if in_tournament:
        print("Pour modifier le classement d'un joueur, au moins un joueur doit être inscrit au tournoi.")
    else:
        print("Pour modifier le classement d'un joueur, au moins un joueur doit être présent dans la base de données.")
    please_continue()


def view_modify_ranking(list_of_players):
    """
    Cette fonction permet à l'utilisateur de voir les informations des joueurs de la liste de joueurs. Il est
    demandé à l'utilisateur de choisir un des joueurs, puis d'écrire le nouveau classement de ce joueur.

    Arg:
        list_of_players = liste de dictionnaire de joueurs.
    Returns:
        modified_player = une liste composée de l'id du joueur et de son nouveau classement.
    """
    print("Joueurs inscrits au tournoi :\n")
    for count, player in enumerate(list_of_players):
        print(str(count + 1) + " - " + player['name'] + " " + player['first_name'] + ", classement : " + str(
            player['ranking']))
    print("\nInscrivez le numéro du joueur dont vous souhaitez modifier le classement :")
    n_player = input()
    correct_input = False
    while not correct_input:
        list_of_valid_choices = [str(count + 1) for count in range(len(list_of_players))]
        if n_player in list_of_valid_choices:
            correct_input = True
            n_player = int(n_player) - 1
        else:
            print("Entrez un chiffre correspondant à un joueur présenté.")
            n_player = input()
    selected_player = list_of_players[n_player]

    print("Entrez le nouveau classement de " + selected_player['name'] + " " + selected_player['first_name'])
    new_ranking = input()
    ranking_is_number = False
    while ranking_is_number is False:
        try:
            new_ranking = int(new_ranking)
            if new_ranking > 0:
                ranking_is_number = True
            else:
                print("Entrez un chiffre positif :")
                new_ranking = input()
        except ValueError:
            print("Entrez un chiffre :")
            new_ranking = input()
    modified_player = [n_player, new_ranking]
    print("Le nouveau classement a bien été enregistré.")
    please_continue()
    return modified_player
