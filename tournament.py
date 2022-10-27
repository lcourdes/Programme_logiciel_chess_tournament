from round import Round


class Tournament:
    """
    Classe qui définit un tournoi.
    """

    def __init__(self, name, place, date_of_tournament, list_of_players, description, number_of_round=4):
        self.name = name
        self.place = place
        self.date_of_tournament = date_of_tournament
        self.list_of_players = list_of_players
        self.description = description
        self.number_of_rounds = number_of_round

        self.list_of_rounds = []
        self.players_score = {}
        self.sorted_player_by_score = {}
        self.all_pairing_matches = []

    def create_players_score(self):
        """
        Cette méthode permet d'initialiser le tableau des scores des joueurs du tournoi.

        Returns:
             players_score est désormais un dictionnaire dans lequel les clés sont les objets joueurs et les valeurs
             sont toutes égales à 0.
        """
        for player in self.list_of_players:
            self.players_score[player] = 0

        return self.players_score

    def create_rounds_of_tournament(self):
        """
        Cette méthode crée une liste des rounds du tournoi.

        Returns:
             self.list_of_rounds = une liste d'objets de la classe Round.
        """
        for i in range(self.number_of_rounds):
            name_of_round = "Round " + str(i + 1)
            self.list_of_rounds.append(Round(name_of_round, self.list_of_players))

        return self.list_of_rounds

    def actualize_players_score(self, results_matches_of_a_round):
        """
        Cette méthode actualise le score des joueurs.

        Args:
            results_matches_of_a_round = liste de résultats obtenue grâce à la méthode get_results_of_round() de
        la classe Round.

        Returns:
             players_score = dictionnaire dont les valeurs sont le résultat des anciens scores additionnés au score
             du round.
        """

        for results_of_match in results_matches_of_a_round:
            for player in results_of_match:
                self.players_score[player[0]] = self.players_score[player[0]] + player[1]

        return self.players_score

    def class_by_score(self):
        """
        Cette méthode permet de classer les joueurs du tournoi en fonction de leur score.

        Returns:
            self.sorted_player_by_score = un dictionnaire dont
                                                - les clefs : sont les différents scores actuels des joueurs.
                                                - les valeurs : une liste des joueurs ayant obtenu ce score.
        """

        score_list = []
        for score in sorted(self.players_score.values(), reverse=True):
            if score not in score_list:
                score_list.append(score)
        for score in score_list:
            players = []
            for player, score_of_player in self.players_score.items():
                if score == score_of_player:
                    players.append(player)
            self.sorted_player_by_score[score] = players

        return self.sorted_player_by_score

    def get_all_pairing_already_established(self):
        """
        Cette méthode permet de lister toutes les paires de joueurs qui se sont déjà affrontés au cours du tournoi.

        Returns:
             self.all_pairing_matches = une liste contenant des sous-listes représentant toutes les paires de
             joueurs qui se sont déjà affrontés eu cours du tournoi.
             [[Joueur_1, Joueur_2], [...]]
        """

        for a_round in self.list_of_rounds:
            for match in a_round.list_of_matches:
                self.all_pairing_matches.append(match.list_of_two_players)

        return self.all_pairing_matches
