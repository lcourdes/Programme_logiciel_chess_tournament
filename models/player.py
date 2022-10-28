class Player:
    """
    CLasse qui définit un joueur.
    """

    def __init__(self, name:str, first_name:str, date_of_birth:str, gender:str, ranking:int):
        self.name = name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking
