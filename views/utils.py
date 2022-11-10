import os
from dateutil.parser import parse, ParserError


def please_continue():
    """
    Cette fonction permet à l'utilisateur de pouvoir voir le message précédent avant d'appuyer sur n'importe quelle
    touche pour effacer le contenu de la fenêtre.
    """
    print("\nAppuyez sur la touche entrée pour continuer.")
    input()
    clear()


def clear():
    """Cette fonction permet d'effacer le contenu de la fenêtre."""
    os.system('clear')


def print_back_data():
    """Cette fonction permet d'informer l'utilisateur qu'une sauvegarde est en cours."""
    print("Sauvegarde en cours...")


def check_input(chosen_option, list_of_valid_choices):
    """
    Cette fonction permet de vérifier qu'un input utilisateur correspond bien à un choix attendu.

    Args:
        chosen_option = input utilisateur.
        list_of_valid_choices = une de choix attendus.

    Returns:
        chosen_option = (integer) le choix de l'utilisateur.
    """
    correct_input = False
    while not correct_input:
        if chosen_option in list_of_valid_choices:
            correct_input = True
        else:
            print("Entrez le chiffre correspondant à un sous-menu.")
            chosen_option = input()
    return int(chosen_option)


def check_date(date):
    """
    Cette fonction permet de vérifier qu'un input correspond bien à un format de date reconnu.

    Arg:
        date = un input utilisateur.

    Returns:
         date = la date est parsée grâce à la librairie dateutil et est retournée au format : jj-mm-aaaa.
    """
    correct_date = False
    while not correct_date:
        try:
            parsed_date = parse(date, dayfirst=True)
            date = parsed_date.strftime("%d-%m-%y")
            correct_date = True
        except ParserError:
            print("La date n'est pas reconnue. Essayez avec le format suivant : jj/mm/aaaa.")
            date = input()
    return date
