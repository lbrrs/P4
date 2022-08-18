from player import Valid
from vues.menu import Views
from model.player import Player


class MenuController:

    def __init__(self):
        self.menu_view = Views()
        self.validator = Valid()

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
        if (response == 'A'):
            self.new_player()
        elif (response == 'B'):
            self.modif_player()
        elif (response == 'C'):
            self.home()

    def new_player(self):
        name = self.validator.get_name()
        firstname = self.validator.get_firstname()
        date = self.validator.get_date()
        sex = self.validator.get_sex()
        rank = self.validator.get_rank()
        print(name, firstname, date, sex, rank)
        Player.save_player(name, firstname, date, sex, rank)


'''
    def modif_player(self):
        #afficher liste joueurs


    def searchByName(self):
        nameSearch = Query()
        db.search(nameSearch.name == reponse)
'''

menu = MenuController()
menu.home()
