from datetime import datetime


def sort_by_ranking(list_of_players):
    """
    Cette fonction permet de classer des joueurs en fonction de leur classement.
    Attention, aux échecs un haut classement est meilleur qu'un plus faible classement. Ainsi, un joueur classé 20
    est mieux classé qu'un joueur classé 10.

    Arg:
        list_of_players: une liste d'instances de Joueurs.

    Returns:
        sorted_players_by_ranking = liste d'instances de Joueurs classés du meilleur classement au moins bon
    classement.
    """

    sorted_players_by_ranking = []
    for player in list_of_players:
        if len(sorted_players_by_ranking) == 0:
            sorted_players_by_ranking.append(player)
        else:
            for n in range(len(sorted_players_by_ranking)+1):
                if n == len(sorted_players_by_ranking):
                    sorted_players_by_ranking.append(player)
                else:
                    if player.ranking > sorted_players_by_ranking[n].ranking:
                        sorted_players_by_ranking.insert(n, player)
                        break
                    else:
                        continue

    return sorted_players_by_ranking


def get_date_and_hour():
    """
    Récupère la date et l'heure actuelle.

    Returns:
        date_and_hour = une liste contenant la date et l'heure actuelle.
    """
    date = datetime.now()
    date_and_hour = [date.strftime("%d-%m-%y"), date.strftime("%H:%M")]

    return date_and_hour
