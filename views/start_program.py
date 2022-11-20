from views.utils import check_input, clear


def view_start_program():
    """
    Cette fonction permet à l'utilisateur de choisir entre :
        - quitter le programme
        - accéder au menu Acteurs (toutes les instances de Joueurs existantes)
        - accéder au menu de gestion de tournoi.

    Returns:
        chosen_option = integer correspondant à l'une des options proposées.
    """
    print("Bienvenue sur le logiciel de gestion de tournoi d'échecs.")
    with open("views/chess_piece.txt", "r") as chess_piece:
        print(chess_piece.read())
    print("Veuillez sélectionner une option ci-dessous en spécifiant le chiffre correspondant.\n")
    print("0 - Quitter le programme.")
    print("1 - Accéder au Menu Acteurs.")
    print("2 - Créer/charger un tournoi")
    user_input = input()
    chosen_option = check_input(user_input, ["0", "1", "2"])
    clear()
    return chosen_option
