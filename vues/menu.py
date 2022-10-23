import re
from model.player import Player

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
        for p in lst_player:
            lst_ser.append(Player.deserialize_player(p))

        while len(lst_ser) >= 8:
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
