import random


class Match:
    """
    Classe qui définit un match.
    """

    def __init__(self, list_of_two_players: list):
        self.list_of_two_players = list_of_two_players
        self.color_distribution = {}
        self.assign_color_to_player()
        self.result = ([], [])

    def assign_color_to_player(self):
        """
        Les couleurs du match sont attribuées aléatoirement aux deux joueurs.

        Returns:
            color_distribution = un dictionnaire dans lequel les couleurs blanche et noire (values) sont reliées aux
            joueurs du match (keys).
        """

        players = [self.list_of_two_players[0], self.list_of_two_players[1]]
        colors = ["blancs", "noirs"]
        random_player = random.choice(players)
        random_color = random.choice(colors)
        players.remove(random_player)
        colors.remove(random_color)
        self.color_distribution = {random_player: random_color, players[0]: colors[0]}

        return self.color_distribution

    def get_result(self, player_id, score):
        """
        Cette méthode permet de stocker le score du match.
        A partir du score de l'un des deux joueurs du match, le score de l'autre joueur est calculé automatiquement.

        Args:
            player_id = l'id d'un joueur.
            score = le score du match du joueur dont l'id est également un argument.

        Returns:
             Un tuple contenant deux listes ([joueur_1, résultat], [joueur_2, résultat])
        """
        if self.list_of_two_players[0].id == player_id:
            result_of_player_1 = [self.list_of_two_players[0], score]
            result_of_player_2 = [self.list_of_two_players[1], 1 - score]
        else:
            result_of_player_1 = [self.list_of_two_players[0], 1 - score]
            result_of_player_2 = [self.list_of_two_players[1], score]

        self.result = (result_of_player_1, result_of_player_2)
        return self.result

    def serialize(self):
        """
        Cette méthode permet de sérialiser l'instance.

        Returns:
             serialized_match = dictionnaire de l'instance.
        """

        serialized_match = {'list_of_two_players': [player.id for player in self.list_of_two_players]}

        if self.color_distribution == {}:
            serialized_match['color_distribution'] = {}
        else:
            serialized_match['color_distribution'] = {player.id: color for player, color in
                                                      self.color_distribution.items()}
        if self.result == ([], []):
            serialized_match['result'] = ([], [])
        else:
            serialized_match['result'] = ([self.result[0][0].id, self.result[0][1]],
                                          [self.result[1][0].id, self.result[1][1]])

        return serialized_match

    @classmethod
    def create_instance(cls, match: dict, list_of_players: list):
        """
        Cette méthode permet de créer une instance de Match à partir d'un dictionnaire d'un match.

        Arg:
            match = un dictionnaire contenant les informations d'un match.
            list_of_players = la liste des joueurs inscrits au tournoi pour lequel le match a été joué.

        Returns:
            une instance de Match.
        """
        two_ids_players = match['list_of_two_players']
        list_of_two_players = []
        for player_id in two_ids_players:
            for player in list_of_players:
                if player.id == player_id:
                    list_of_two_players.append(player)
        created_match = cls(list_of_two_players)
        color_distribution = {}
        if match['color_distribution'] != {}:
            for player_id, color in match['color_distribution'].items():
                for player in list_of_players:
                    if int(player_id) == player.id:
                        color_distribution[player] = color
        created_match.color_distribution = color_distribution

        result = []
        if match['result'] != [[], []]:
            for result_of_player in match['result']:
                for player in list_of_players:
                    if result_of_player[0] == player.id:
                        result.append([player, result_of_player[1]])
        else:
            result = [[], []]
        created_match.result = tuple(result)

        return created_match
