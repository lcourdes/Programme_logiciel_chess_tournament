from tinydb import TinyDB
from utils import get_date_and_hour
from models.round import Round
from models.player import Player


class Tournament:
    """
    Classe qui définit un tournoi.
    """

    def __init__(self, name: str, place: str, date_of_tournament: str, description: str, number_of_rounds: int = 4):
        self.name = name
        self.place = place
        self.date_of_tournament = date_of_tournament
        self.list_of_players = []
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.db = TinyDB('db.json')

        self.creation_date = get_date_and_hour()
        self.list_of_rounds = []
        self.players_score = {}
        self.sorted_player_by_score = {}
        self.all_pairing_matches = []

    def create_rounds(self):
        """
        Cette méthode crée une liste des rounds du tournoi.

        Returns:
             self.list_of_rounds = une liste d'objets de la classe Round.
        """
        for i in range(self.number_of_rounds):
            name_of_round = "Round " + str(i + 1)
            self.list_of_rounds.append(Round(name=name_of_round, list_of_players=self.list_of_players))

        return self.list_of_rounds

    def get_players_score(self):
        """
        Cette méthode actualise le score des joueurs.

        Returns:
             self.players_score = dictionnaire dont les clés correspondent aux joueurs et les valeurs au calcul des
             scores sur l'ensemble des matches joués.
        """
        players_score = {}
        for player in self.list_of_players:
            players_score[player] = 0

        for round in self.list_of_rounds:
            results_matches_of_a_round = round.get_results()
            if results_matches_of_a_round != []:
                for results_of_match in results_matches_of_a_round:
                    for player in results_of_match:
                        players_score[player[0]] = players_score[player[0]] + player[1]

        self.players_score = players_score
        return self.players_score

    def sort_by_score(self):
        """
        Cette méthode permet de classer les joueurs du tournoi en fonction de leur score.

        Returns:
            self.sorted_player_by_score = un dictionnaire dont
                                                - les clefs : sont les différents scores actuels des joueurs.
                                                - les valeurs : une liste des joueurs ayant obtenu ce score.
        """

        self.get_players_score()
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

    def serialize(self):
        """
        Cette méthode permet de sérialiser l'instance.

        Returns:
             serialized_tournament = dictionnaire de l'instance.
        """
        serialized_tournament = {'name': self.name,
                                 'place': self.place,
                                 'date_of_tournament': self.date_of_tournament,
                                 'creation_date': self.creation_date,
                                 'description': self.description,
                                 'number_of_rounds': self.number_of_rounds
                                 }

        if self.list_of_rounds == []:
            serialized_tournament['list_of_rounds'] = []
        else:
            serialized_tournament['list_of_rounds'] = [round.serialize() for round in self.list_of_rounds]

        if self.players_score == {}:
            serialized_tournament['players_score'] = {}
        else:
            serialized_tournament['players_score'] = {player.id: score for player, score in self.players_score.items()}

        return serialized_tournament

    def back_up_data(self):
        """
        Cette fonction permet de sauvegarder les informations des joueurs et du tournoi dans une table 'players' et
        'tournament' TinyDB.
        """
        players_table = self.db.table('players')
        players_table.truncate()
        serialized_players = []
        for player in self.list_of_players:
            serialized_players.append(player.serialize())
        players_table.insert_multiple(serialized_players)
        for index, player in enumerate(self.list_of_players):
            player.id = index + 1

        tournament_table = self.db.table('tournament')
        tournament_table.truncate()
        tournament_table.insert(self.serialize())
