"""
Ce poc permet de créer un tournoi et d'y ajouter huit joueurs.
Après avoir affiché les informations principales du tournoi, les deux premiers rounds sont créés. Pour chacun d'eux,
les résultats des matchs sont tirés au hasard.
"""

from models.player import Player
from models.tournament import Tournament
import random


player_1 = {"name": "Dupont", "first_name": "Jean", "date_of_birth": "10-10-45", "gender": "homme", "ranking": 67}
player_2 = {"name": "Martin", "first_name": "Jeanne", "date_of_birth": "01-04-78", "gender": "femme", "ranking": 74}
player_3 = {"name": "Li", "first_name": "Thibault", "date_of_birth": "30-05-58", "gender": "homme", "ranking": 24}
player_4 = {"name": "Smith", "first_name": "John", "date_of_birth": "16-06-67", "gender": "homme", "ranking": 93}
player_5 = {"name": "Mohammed", "first_name": "Sandra", "date_of_birth": "14-02-74", "gender": "femme", "ranking": 61}
player_6 = {"name": "Rodriguez", "first_name": "Robert", "date_of_birth": "03-03-53", "gender": "homme", "ranking": 2}
player_7 = {"name": "Kim", "first_name": "Ali", "date_of_birth": "22-09-98", "gender": "homme", "ranking": 30}
player_8 = {"name": "Murphy", "first_name": "Marie", "date_of_birth": "07-07-81", "gender": "femme", "ranking": 82}

list_of_hand_made_players = [player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8]
list_of_players = [Player.create_instance(player) for player in list_of_hand_made_players]

tournament = Tournament("Tournoi d'échecs 2022",
                        "Paris",
                        ["20-10-23", "22-10-23"],
                        "Ce tournoi rassemble les plus grands pontes.",
                        "Blitz")
tournament.list_of_players = list_of_players

# Affichage des informations principales du tournoi
print("Nom du tournoi : " + tournament.name)
print("Lieu du tournoi : " + tournament.place)
print("Date du tournoi : " + tournament.date_of_tournament[0] + " - " + tournament.date_of_tournament[1])
print("Description : " + tournament.description)
print("Type de jeu : " + tournament.game_type)

# Affichage des scores au début du tournoi
tournament.get_players_score()
print("\nScore du tournoi : ")
for player, score in tournament.players_score.items():
    print(player.name + " " + player.first_name + ": " + str(score) + " points.")

# Création des rounds du tournoi
tournament.create_rounds()

# Création des matchs du premier round
tournament.list_of_rounds[0].first_round_pairing()
matches_of_first_round = tournament.list_of_rounds[0].create_matches()
for match in matches_of_first_round:
    match.assign_color_to_player()

# Affichage des informations du premier round
print("\n" + tournament.list_of_rounds[0].name)
for count, match in enumerate(matches_of_first_round):
    count += 1
    print("> Match " + str(count))
    player_1 = match.list_of_two_players[0]
    player_2 = match.list_of_two_players[1]
    print(player_1.name + " " + player_1.first_name + " (" + str(player_1.ranking) + ")"
          + " doit jouer les " + match.color_distribution[player_1])
    print(player_2.name + " " + player_2.first_name + " (" + str(player_2.ranking) + ")"
          + " doit jouer les " + match.color_distribution[player_2])

# Chaque match reçoit un résultat aléatoire
for match in matches_of_first_round:
    result_of_player_1 = [match.list_of_two_players[0], random.choice([0, 0.5, 1])]
    result_of_player_2 = []
    if result_of_player_1[1] == 0:
        result_of_player_2 = [match.list_of_two_players[1], 1]
    elif result_of_player_1[1] == 0.5:
        result_of_player_2 = [match.list_of_two_players[1], 0.5]
    elif result_of_player_1[1] == 1:
        result_of_player_2 = [match.list_of_two_players[1], 0]
    match.result = (result_of_player_1, result_of_player_2)
tournament.list_of_rounds[0].get_results()

# Affichage des résultats du premier round
results_of_matches = tournament.list_of_rounds[0].results_of_matches
print("\nRésultats des matchs du " + tournament.list_of_rounds[0].name)
for count, result in enumerate(results_of_matches):
    count += 1
    print("> Match " + str(count) + " : "
          + result[0][0].name + " " + result[0][0].first_name
          + " versus "
          + result[1][0].name + " " + result[1][0].first_name
          + " : " + str(result[0][1]) + " : " + str(result[1][1]))

# Affichage des scores du tournoi
tournament.get_players_score()
print("\nScore du tournoi : ")
for player, score in tournament.players_score.items():
    print(player.name + " " + player.first_name + ": " + str(score) + " points.")

# Création des matchs du second round
all_matches = tournament.get_all_pairing_already_established()
sorted_player_by_score = tournament.sort_by_score()
tournament.list_of_rounds[1].other_round_pairing(sorted_player_by_score, all_matches)
matches_of_second_round = tournament.list_of_rounds[1].create_matches()
for match in matches_of_second_round:
    match.assign_color_to_player()

# Affichage des informations du premier round
print("\n" + tournament.list_of_rounds[1].name)
for count, match in enumerate(matches_of_second_round):
    count += 1
    print("> Match " + str(count))
    player_1 = match.list_of_two_players[0]
    player_2 = match.list_of_two_players[1]
    print(player_1.name + " " + player_1.first_name + " (" + str(player_1.ranking) + ")"
          + " doit jouer les " + match.color_distribution[player_1])
    print(player_2.name + " " + player_2.first_name + " (" + str(player_2.ranking) + ")"
          + " doit jouer les " + match.color_distribution[player_2])

# Chaque match reçoit un résultat aléatoire
for match in matches_of_second_round:
    result_of_player_1 = [match.list_of_two_players[0], random.choice([0, 0.5, 1])]
    result_of_player_2 = []
    if result_of_player_1[1] == 0:
        result_of_player_2 = [match.list_of_two_players[1], 1]
    elif result_of_player_1[1] == 0.5:
        result_of_player_2 = [match.list_of_two_players[1], 0.5]
    elif result_of_player_1[1] == 1:
        result_of_player_2 = [match.list_of_two_players[1], 0]
    match.result = (result_of_player_1, result_of_player_2)
tournament.list_of_rounds[1].get_results()

# Affichage des résultats du premier round
results_of_matches = tournament.list_of_rounds[1].results_of_matches
print("\nRésultats des matchs du " + tournament.list_of_rounds[1].name)
for count, result in enumerate(results_of_matches):
    count += 1
    print("> Match " + str(count) + " : "
          + result[0][0].name + " " + result[0][0].first_name
          + " versus "
          + result[1][0].name + " " + result[1][0].first_name
          + " : " + str(result[0][1]) + " : " + str(result[1][1]))

# Affichage des scores du tournoi
tournament.get_players_score()
print("\nScore du tournoi : ")
for player, score in tournament.players_score.items():
    print(player.name + " " + player.first_name + ": " + str(score) + " points.")

"""
Pour terminer le tournoi, il suffit de répéter le processus effectué sur le second round pour tous les rounds restants.
"""
