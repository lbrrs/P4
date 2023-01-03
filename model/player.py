from tinydb import TinyDB, Query



class Player:
    def __init__(self, name, firstname, date, sex, rank):

        self.name = name
        self.firstname = firstname
        self.date = date
        self.sex = sex
        self.rank = rank

    def __str__(self):
        return self.name, self.firstname, self.date, self.sex, self.rank

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
    def save_player(nom, firstname, date, sex, rank):
        db = TinyDB("../data.json")
        player_db = db.table("Players")
        player_db.insert(Player.serialized_player(nom, firstname, date, sex, rank))

    @staticmethod
    def deserialize_player(documents):
        lst = list()
        for document in documents:
            lst.append(Player(document["name"], document["firstname"], document["date"], document["sex"], document["rank"]))
        return lst



