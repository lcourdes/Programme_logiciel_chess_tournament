from Autres import *
from match import Match


class Round:
    """
    Classe qui définit un tour de tournoi.
    """

    def __init__(self, name, list_of_players):
        self.name = name
        self.list_of_players = list_of_players
        self.pairing_players = []
        self.list_of_matches = []
        self.results_of_matches = []

    def first_round_pairing(self):
        """
        Cette méthode permet de créer les appariements de joueurs pour un premier tour de tournoi.
        - Les joueurs sont triés en fonction du classement en faisant appel à la fonction 'class_by_ranking()'.
        - La liste obtenue est divisée en deux groupes.
        - Les joueurs sont appariés de la manière suivante : les premiers de chacune des listes, les deuxièmes de
        chacune des listes, les troisièmes de chacune des listes, etc.

        Returns:
            pairing_players = une liste contenant des sous-listes. Les sous-listes sont composées de
                                            deux joueurs qui doivent s'affronter pour le prochain match.
                                            [[Joueur_1, Joueur_2], [...]]
        """

        sorted_players_by_ranking = class_by_ranking(self.list_of_players)
        n = len(sorted_players_by_ranking) // 2
        sorted_players_by_ranking_first_group = sorted_players_by_ranking[:n]
        sorted_players_by_ranking_second_group = sorted_players_by_ranking[n:]
        self.pairing_players = [[i, j] for i, j in zip(sorted_players_by_ranking_first_group,
                                                       sorted_players_by_ranking_second_group)]

        return self.pairing_players

    def other_round_pairing(self, sorted_player_by_score, all_pairing_already_established):
        """
        Cette méthode permet de créer les appariements de joueurs pour les deuxièmes tours et suivants.
        - Les joueurs du tournoi sont ajoutés dans la liste list_of_players.
            (1) des joueurs ayant le score le plus élevé jusqu'au score le plus faible
            (2) Pour des scores identiques les joueurs sont triés en fonction du classement
        - Le premier joueur de la list_of_player est apparié avec un joueur :
            (1) Si la paire ne s'est pas déjà rencontrée au cours d'un match les joueurs sont appariés dans la liste
            self.pairing_players et ils sont supprimés de la liste list_of_players.
            (2) Si la paire s'est déjà rencontrée on teste l'appariement entre le premier joueur de la liste
                # list_of_player avec le joueur suivant.
        Args :
            sorted_player_by_score : dictionnaire obtenu grâce à la méthode class_by_score() de la classe Tournament.

            all_pairing_already_established : liste obtenue grâce à la méthode get_all_pairing_already_established()
                                                de la classe Tournament.
        Returns:
            pairing_players = une liste contenant des sous-listes. Les sous-listes sont composées de
                                            deux joueurs qui doivent s'affronter pour le prochain match.
                                            [[Joueur_1, Joueur_2], [...]]
        """
        list_of_players = []
        for score, players in sorted_player_by_score.items():
            if len(players) > 1:
                sorted_players_by_ranking = class_by_ranking(players)
                list_of_players = list_of_players + sorted_players_by_ranking
            else:
                list_of_players.append(players[0])

        while len(list_of_players) > 0:
            for i in range(1, len(list_of_players)):
                test_appairing = [list_of_players[0], list_of_players[i]]
                if test_appairing not in all_pairing_already_established:
                    self.pairing_players.append(test_appairing)
                    del list_of_players[i]
                    del list_of_players[0]
                    break
        return self.pairing_players

    def create_matches_of_round(self):
        """
        Cette méthode permet de créer des matchs à partir de la liste 'pairing_players' obtenue par une méthode
        d'appariement (soit first_round_pairing(), soit other_round_pairing()).

        Returns:
             Un tuple contenant les objets matchs du tour.
        """

        for pair_of_player in self.pairing_players:
            match = Match(pair_of_player)
            self.list_of_matches.append(match)

        return self.list_of_matches

    def get_results_of_round(self):
        """
        Cette méthode permet de récupérer les résultats de tous les matchs du round.

        Returns:
             self.results_of_matches = une liste contenant les résultats de chaque match stocké dans des tuples.
                                        [([Joueur, Score], [Joueur, Score]), (), ...]
        """
        for match in self.list_of_matches:
            result = match.get_result()
            self.results_of_matches.append(result)

        return self.results_of_matches
