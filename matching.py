from tinydb import TinyDB, Query, where

from model.player import Player
from model.model import Match
from model.model import Round
import datetime

class Matching:

    def __init__(self, roundnumber):
        self.round = Round(datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(hours=2), roundnumber)

    def match_players(self, lstPlrT):
        lst_rank = []
        lstPlrT = Player.deserialize_player(lstPlrT)
        lstPlrT.sort(key=lambda x: x.rank)
        for player in lstPlrT:
            lst_rank.append(player)
        lst_match = [(lst_rank[0], lst_rank[4]), (lst_rank[1], lst_rank[5]), (lst_rank[2], lst_rank[6]),
                     (lst_rank[3], lst_rank[7])]
        self.round.match.append(lst_match)
        return lst_match


