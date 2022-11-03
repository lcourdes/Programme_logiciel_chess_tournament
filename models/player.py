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
