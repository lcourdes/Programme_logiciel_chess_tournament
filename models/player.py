class Player:
    """
    CLasse qui définit un joueur.
    """

    def __init__(self, name: str, first_name: str, date_of_birth: str, gender: str, ranking: int):
        self.name = name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking

        self.id = None

    def assign_id(self, list_of_actors):
        self.id = len(list_of_actors)

    def modify_ranking(self, new_ranking):
        """
        Cette méthode permet de mettre à jour le classement d'un joueur.
        Arg:
            new_ranking: un chiffre positif qui correspond au classement actualisé d'un joueur.
        Returns:
             self.ranking = classement actualisé.
        """
        self.ranking = new_ranking
        return self.ranking

    def serialize(self):
        """
        Cette méthode permet de sérialiser l'instance.

        Returns:
             serialized_player = dictionnaire de l'instance.
        """
        serialized_player = {
            'name': self.name,
            'first_name': self.first_name,
            'date_of_birth': self.date_of_birth,
            'gender': self.gender,
            'ranking': self.ranking
        }

        return serialized_player

    @classmethod
    def create_instance(cls, player_dict):
        """
        Cette méthode permet de créer une instance de Player à partir d'un dictionnaire d'un joueur.

        Arg:
            player_dict = un dictionnaire contenant les informations d'un joueur.

        Returns:
            une instance de Player.
        """
        name = player_dict['name']
        first_name = player_dict['first_name']
        date_of_birth = player_dict['date_of_birth']
        gender = player_dict['gender']
        ranking = player_dict['ranking']

        return cls(name, first_name, date_of_birth, gender, ranking)
