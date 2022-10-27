import random


class Match:
    """
    Classe qui définit un match.
    """

    def __init__(self, list_of_two_players):
        self.list_of_two_players = list_of_two_players
        self.assign_color_to_player()
        self.color_distribution = {}
        self.result = ()

    def assign_color_to_player(self):
        """
        Les couleurs du match sont attribuées aléatoirement aux deux joueurs.

        Returns:
            color_distribution = un dictionnaire dans lequel les couleurs blanche et noire (values) sont reliées aux
            joueurs du match (keys).
        """

        players = [self.list_of_two_players[0], self.list_of_two_players[1]]
        colors = ["white", "black"]
        random_player = random.choice(players)
        random_color = random.choice(colors)
        players.remove(random_player)
        colors.remove(random_color)
        self.color_distribution = {random_player: random_color, players[0]: colors[0]}

        return self.color_distribution

    def get_result(self):
        """
        Pour l'instant cette méthode détermine aléatoirement le résultat du match.

        Returns:
             Un tuple contenant deux listes ([joueur_1, résultat], [joueur_2, résultat])
        """

        result_of_player_1 = [self.list_of_two_players[0], random.choice([0, 0.5, 1])]
        result_of_player_2 = []

        if result_of_player_1[1] == 0:
            result_of_player_2 = [self.list_of_two_players[1], 1]
        elif result_of_player_1[1] == 0.5:
            result_of_player_2 = [self.list_of_two_players[1], 0.5]
        elif result_of_player_1[1] == 1:
            result_of_player_2 = [self.list_of_two_players[1], 0]
        result = (result_of_player_1, result_of_player_2)

        return result
