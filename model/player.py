from tinydb import TinyDB, Query
from Views


class Player:
    def __init__(self, name, firstname, date, sex, rank):
        self.name = name
        self.firstname = firstname
        self.date = date
        self.sex = sex
        self.rank = rank

    @staticmethod
    def serialized_player(nom, firstname, date, sex, rank):
        ser_player = {
            #id
            "name": nom,
            "firstname": firstname,
            "date": date,
            "sex": sex,
            "rank": rank,
        }
        return ser_player

    @staticmethod
    def save_player(self, nom, firstname, date, sex, rank):
        db = TinyDB("player.json")
        db.insert(self.serialized_player(nom, firstname, date, sex, rank))

    def searchByName(self):
        nameSearch = Query()
        db.search(nameSearch.name == reponse)
