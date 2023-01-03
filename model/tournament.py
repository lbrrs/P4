from tinydb import TinyDB


class Tournament:
    def __init__(self, name, place, date, nbRounds, player, round, time, description, actual_rounds):
        self.name = name
        self.place = place
        self.date = date
        self.nbRounds = nbRounds
        self.round = round
        self.player = player
        self.time = time
        self.description = description
        self.actual_rounds = actual_rounds

    def __str__(self):
        return self.name, self.place, self.date, self.nbRounds, self.round, self.player, self.time, self.description, self.actual_rounds

    @staticmethod
    def serialized_tournament(name, place, date, nbRounds, round, time, player=None, description='', actual_rounds=1):
        ser_tournament = {
            "name": name,
            "place": place,
            "date": date,
            "nbRounds": nbRounds,
            "round": round,
            "player": player,
            "time": time,
            "description": description,
            "actual_rounds": actual_rounds
        }
        return ser_tournament


    @staticmethod
    def save_tournament(name, place, date, round, nbRounds, time, player=None, description='', actual_rounds=1):
        db = TinyDB("../data.json")
        tournament_db = db.table("Tournaments")
        tournament_db.insert(Tournament.serialized_tournament(name, place, date, round, nbRounds, time, player, description, actual_rounds))

    @staticmethod
    def deserialize_player(document):
        player = Tournament(document["name"], document["firstname"], document["date"], document["sex"], document["rank"])
        return player

    @staticmethod
    def deserialize_tournament(document):
        tournament = Tournament(document["name"], document["place"], document["date"], document["round"], document["nbRounds"], document["time"], document["player"], document["description"], document["actual_rounds"])
        return tournament
