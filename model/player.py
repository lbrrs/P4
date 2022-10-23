from tinydb import TinyDB, Query



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
    def save_player(nom, firstname, date, sex, rank):
        db = TinyDB("../players.json")
        db.insert(Player.serialized_player(nom, firstname, date, sex, rank))


    @staticmethod
    def deserialize_player(document):
        player = Player(document["name"], document["firstname"], document["date"], document["sex"], document["rank"])
        return player



