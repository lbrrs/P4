from tinydb.operations import delete

from player import Valid
from tournament import Tournoi
from vues.menu import Views
from model.player import Player
from model.tournament import Tournament
from tinydb import TinyDB, Query, where
from tinydb.operations import delete


class MenuController:

    def __init__(self):
        self.menu_view = Views()
        self.validator = Valid()
        self.validator_t = Tournoi()


    def home(self):
        menu = {
            '1': 'Gestion des joueurs',
            '2': 'Gestions des tournois',
            '3': 'Quitter'
        }
        response = self.menu_view.display_menu(menu)
        if response == '1':
            self.players_gestion()
        elif response == '2':
            self.tournament_gestion()

    def players_gestion(self):
        menu = {
            'A': 'Créer un joueur',
            'B': 'Modifier un joueur',
            'C': 'Accueil'
        }
        response = self.menu_view.display_menu(menu)
        if response == 'A':
            self.new_player()
        elif response == 'B':
            lst_player = self.modif_player()
            player = self.menu_view.display_player(lst_player)
            self.choose_modif(player)
        elif response == 'C':
            self.home()

    def new_player(self):
        name = self.validator.get_name()
        firstname = self.validator.get_firstname()
        date = self.validator.get_date()
        sex = self.validator.get_sex()
        rank = self.validator.get_rank()
        print(name, firstname, date, sex, rank)
        Player.save_player(name, firstname, date, sex, rank)

    def modif_player(self):
        # afficher liste joueurs
        db = TinyDB('../players.json')
        table = db.all()
        return table

    def choose_modif(self, player):
        db = TinyDB('../players.json')
        db.remove(where('name') == player['name'])
        self.new_player()

    def tournament_gestion(self):
        menu = {
            'D': 'Créer un tournoi',
            'E': 'Reprendre un tournoi',
            'F': 'Supprimer un tournoi',
            'G': 'Quitter'
        }
        response = self.menu_view.display_menu(menu)
        if response == 'D':
            lst_player = self.modif_player()
            addPlayer = self.menu_view.display_players_tournament(lst_player)
            self.new_tournament(addPlayer)
        elif response == 'E':
            self.modif_tournament()
        elif response == 'F':
            self.del_tournament()
        elif response == 'G':
            self.home()

    def new_tournament(self, addPlayer):
        name = self.validator_t.get_name_t()
        place = self.validator_t.get_place()
        date = self.validator_t.get_date_t()
        nbRounds = self.validator_t.get_nbRounds()
        time = self.validator_t.get_time()
        description = self.validator_t.get_description()
        player = list(addPlayer)
        Tournament.save_tournament(name, place, date, [], nbRounds, time, player, description)


menu = MenuController()
menu.home()
