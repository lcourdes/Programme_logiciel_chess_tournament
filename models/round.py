from utils import sort_by_ranking
from models.match import Match


class Round:
    """
    Classe qui définit un tour de tournoi.
    """

    def __init__(self, name: str, list_of_players: list):
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

        sorted_players_by_ranking = sort_by_ranking(self.list_of_players)
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
                sorted_players_by_ranking = sort_by_ranking(players)
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

    def create_matches(self):
        """
        Cette méthode permet de créer des matchs à partir de la liste 'pairing_players' obtenue par une méthode
        d'appariement (soit first_round_pairing(), soit other_round_pairing()).

        Returns:
             Un tuple contenant les objets matchs du tour.
        """

        for pair_of_player in self.pairing_players:
            match = Match(list_of_two_players=pair_of_player)
            self.list_of_matches.append(match)

        return self.list_of_matches

    def get_results(self):
        """
        Cette méthode permet de récupérer les résultats de tous les matchs du round.

        Returns:
             self.results_of_matches = une liste contenant les résultats de chaque match stocké dans des tuples.
                                        [([Joueur, Score], [Joueur, Score]), (), ...]
        """
        self.results_of_matches = []
        for match in self.list_of_matches:
            result = match.result
            self.results_of_matches.append(result)
        return self.results_of_matches

    def serialize(self):
        """
        Cette méthode permet de sérialiser l'instance.

        Returns:
             serialized_round = dictionnaire de l'instance.
        """
        serialized_round = {'name': self.name}

        if self.pairing_players == []:
            serialized_round['pairing_players'] = []
        else:
            players = []
            for pair_of_players in self.pairing_players:
                pair = [pair_of_players[0].id, pair_of_players[1].id]
                players.append(pair)
            serialized_round['pairing_players'] = players

        if self.list_of_matches == []:
            serialized_round['list_of_matches'] = []
        else:
            all_matches = [match.serialize() for match in self.list_of_matches]
            serialized_round['list_of_matches'] = all_matches

        return serialized_round

    @classmethod
    def create_instance(cls, round_dict: dict, list_of_players: list):
        """
        Cette méthode permet de créer une instance de Round à partir d'un dictionnaire d'un round.

        Arg:
            round = un dictionnaire contenant les informations d'un round.
            list_of_players = la liste des objets joueurs.

        Returns:
            une instance de Round.
        """
        name = round_dict['name']
        created_round = cls(name, list_of_players)

        all_pairing = round_dict['pairing_players']
        pairing_players = []
        for ids in all_pairing:
            pair = []
            for player in list_of_players:
                if player.id in ids:
                    pair.append(player)
            pairing_players.append(pair)
        created_round.pairing_players = pairing_players

        list_of_matches = []
        for match_dict in round_dict['list_of_matches']:
            match = Match.create_instance(match_dict, list_of_players)
            list_of_matches.append(match)
        created_round.list_of_matches = list_of_matches

        created_round.results_of_matches = [match.result for match in list_of_matches]

        return created_round
