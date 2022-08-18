from controllers.menu import MenuController
import re


class Valid:

    def __init__(self):
        self.menu_control = MenuController()

    #Name
    def is_valid_name(name):
        # regex
        pattern = '^[a-zA-Z]+$'
        re.match(pattern, name)
        return name.is_valid_name(name)


    def get_name(self):
        name = input("name :")
        if self.is_valid_name(name):
            return name
        print('Invalid name')
        return self.get_name()


    #Firstname
    def is_valid_firstname(firstname):
        # regex
        pattern = '^[a-zA-Z]+$'
        re.match(pattern, firstname)
        return firstname.is_valid_name(firstname)


    def get_firstname(self):
        firstname = input("firstname :")
        if self.is_valid_firstname(firstname):
            return firstname
        print('Invalid firstname')
        return self.get_firstname()


    #Date
    def is_valid_date(date):
        # regex
        pattern = '^[0-9]+$'
        re.match(pattern, date)
        return date.is_valid_date(date)


    def get_date(self):
        date = input("date :")
        if self.is_valid_name(date):
            return date
        print('Invalid date')
        return self.get_date()

    #Sex
    def is_valid_sex(sex):
        # regex
        pattern = '^[a-zA-Z]+$'
        re.match(pattern, sex)
        return sex.is_valid_sex(sex)


    def get_sex(self):
        name = input("sex :")
        if self.is_valid_sex(sex):
            return sex
        print('Invalid sex')
        return self.get_sex()

    # rank
    def is_valid_rank(rank):
        # regex
        pattern = '^[a-zA-Z]+$'
        re.match(pattern, rank)
        return is_valid_rank(rank)

    def get_rank(self):
        name = input("rank :")
        if self.is_valid_rank(rank):
            return rank
        print('Invalid rank')
        return self.get_rank()