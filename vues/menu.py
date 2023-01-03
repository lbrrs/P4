import re
from model.player import Player
from model.model import Match
from matching import Matching

class Views:

    def __init__(self):
        pass

    @staticmethod
    def display_menu(menu):
        for index, choice in menu.items():
            print(index, ')', choice)
        response = input('Choix : ')
        if response in menu:
            return response
        print('Choix incorrect')
        return Views.display_menu(menu)

    @staticmethod
    def display_menubis(menu):
        for index, choice in menu:
            print(index,')', choice)
        reponse = input('Choix : ')
        if reponse in menu:
            return reponse
        print('Choix incorrect')
        return Views.display_menubis(menu)

    @staticmethod
    def display_player(lst_player):
        for count, player in enumerate(lst_player, 1):
            print(f'{count}: {player}')
        reponse = input('Choix : ')
        if int(reponse) <= len(lst_player):
            print(lst_player[int(reponse)-1])
        else:
            print('Choix incorrect')
        return lst_player[int(reponse)-1]

    @staticmethod
    def display_tournament(menu, lst_player):
        for index, choice in menu:
            print(index,')', choice)
        reponse = input('Choix : ')
        if reponse in menu:
            return reponse
        print('Choix incorrect')
        return Views.display_menubis(menu)

    @staticmethod
    def display_tournaments(menu):
        for index, choice in menu:
            print(index,')', choice)
        reponse = input('Choix : ')
        if reponse in menu:
            return reponse
        print('Choix incorrect')

    @staticmethod
    def display_players_tournament(lst_player):
        lst_ser = list()
        while len(lst_ser) < 8:
            for count, player in enumerate(lst_player, 1):
                print(f'{count}: {player}')
            len_prev = len(lst_ser)
            pattern = '[0-9]{1}'
            pattern1 = '[0-9]{2}'
            reponse = input('Choix : ')
            if re.match(pattern, reponse) is not None or re.match(pattern1, reponse) is not None:
                lst_ser.append(reponse)

            if len(lst_ser) > len_prev:
                print(lst_ser)
            else:
                print('Choix incorrect')
        return lst_ser

    @staticmethod
    def display_tournament_modif(lst_tournament):
        for count, tournament in enumerate(lst_tournament, 1):
            print(f'{count}: {tournament}')
        reponse = input('Choix : ')
        if int(reponse) <= len(lst_tournament):
            print(lst_tournament[int(reponse)-1])
        else:
            print('Choix incorrect')
        return lst_tournament[int(reponse)-1]

    def display_tournament_result(self, round):
        for count, matching in enumerate(round.match, 1):
            print(f'{count}: {matching[0].__str__()}'),
            print(f'{count}: {matching[1].__str__()}')
            reponse1 = input('1 = Victoire Joueur 1, 2 = Victoire Joueur 2, 3 = Match nul \n Resultat : ')
            matching.result = reponse1
            if reponse1 not in [1, 2, 3]:
                print('Choix incorrect')
                return self.display_tournament(round)
        return round
