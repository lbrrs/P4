# from controllers.menu import MenuController
import re
from datetime import datetime

class Valid:

    def __init__(self):
        # self.menu_control = MenuController()
        pass

    #Name
    def is_valid_name(self, name):
        # regex
        pattern = '^[a-zA-Z]+$'
        return re.match(pattern, name)


    def get_name(self):
        name = input("name :")
        if self.is_valid_name(name):
            return name
        print('Invalid name')
        return self.get_name()


    #Firstname
    def is_valid_firstname(self, firstname):
        # regex
        pattern = '^[a-zA-Z]+$'
        return re.match(pattern, firstname)


    def get_firstname(self):
        firstname = input("firstname :")
        if self.is_valid_firstname(firstname):
            return firstname
        print('Invalid firstname')
        return self.get_firstname()


    #Date
    def is_valid_date(self, date):
        # regex
        try:
            pattern = datetime.strptime(date, '%m-%d-%Y').date()
            return True
        except ValueError:
            return False



    def get_date(self):
        date = input("date :")
        if self.is_valid_date(date):
            return date
        print('Invalid date')
        return self.get_date()

    #Sex
    def is_valid_sex(self, sex):
        # regex
        pattern = '^[a-zA-Z]+$'
        return re.match(pattern, sex)

    def get_sex(self):
        sex = input("sex :")
        if self.is_valid_sex(sex):
            return sex
        print('Invalid sex')
        return self.get_sex()

    # rank
    def is_valid_rank(self, rank):
        # regex
        pattern = '[0-9]{4}'
        return re.match(pattern, rank)

    def get_rank(self):
        rank = input("rank :")
        if self.is_valid_rank(rank):
            return rank
        print('Invalid rank')
        return self.get_rank()
