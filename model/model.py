class Player:
    def __init__(self, name, firstname, date, sex, rank):
        self.name = name
        self.firstname = firstname
        self.date = date
        self.sex = sex
        self.rank = rank


class Tournoi:
    def __init__(self, name, place, date, rounds, time, description):
        self.name = name
        self.place = place
        self.date = date
        self.rounds = rounds
        self.round = []
        self.player = []
        self.time = time
        self.description = description
        self.actual_rounds = 1


class Round:
    def __init__(self, name, date_start, date_end):
        self.name = name
        self.date_start = date_start
        self.date_end = date_end
        self.match = []


class Match:

    def __init__(self, result):
        self.result = result
        self.player = []
