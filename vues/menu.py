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


