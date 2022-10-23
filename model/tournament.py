from tinydb import TinyDB


class Tournament:
    def __init__(self, name, place, date, nbRounds, player, round, time, description):
        self.name = name
        self.place = place
        self.date = date
        self.nbRounds = nbRounds
        self.round = round
        self.player = player
        self.time = time
        self.description = description

    @staticmethod
    def serialized_tournament(name, place, date, nbRounds, round, time, player=None, description=''):
        ser_tournament = {
            "name": name,
            "place": place,
            "date": date,
            "nbRounds": nbRounds,
            "round": round,
            "player": player,
            "time": time,
            "description": description,
        }
        return ser_tournament


    @staticmethod
    def save_tournament(name, place, date, round, nbRounds, time, player=None, description=''):
        db = TinyDB("../tournament.json")
        db.insert(Tournament.serialized_tournament(name, place, date, round, nbRounds, time, player, description))
