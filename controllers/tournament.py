import re
from datetime import datetime

class Tournoi:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        pass

    def is_valid_name_t(self, name):
        # regex
        pattern = '^[a-zA-Z]+$'
        return re.match(pattern, name)

    def get_name_t(self):
        name = input("name :")
        if self.is_valid_name_t(name):
            return name
        print('Invalid name')
        return self.get_name_t()

    def is_valid_place (self, place):
        pattern = '^[a-zA-Z]+$'
        return re.match(pattern, place)

    def get_place(self):
        place = input("place :")
        if self.is_valid_place(place):
            return place
        print('Invalid place')
        return self.get_place()

    def is_valid_date_t(self, date):
        try:
            pattern = datetime.strptime(date, '%m-%d-%Y').date()
            return True
        except ValueError:
            return False

    def get_date_t(self):
        date = input("date :")
        if self.is_valid_date_t(date):
            return date
        print('Invalid date')
        return self.get_date_t()

    def is_valid_nbRounds(self, nbRounds):
        pattern = '[0-9]'
        return re.match(pattern, nbRounds)

    def get_nbRounds(self):
        nbRounds = input("nbRounds :")
        if self.is_valid_nbRounds(nbRounds):
            return nbRounds
        return self.get_nbRounds()

    def is_valid_time(self, time):
        pattern = '(bullet)|(blitz)|(coup rapide)'
        return re.match(pattern, time)

    def get_time(self):
        time = input("time :")
        if self.is_valid_time(time):
            return time
        return self.get_time()

    def is_valid_description(self, description):
        pattern = '^[a-zA-Z]+$'
        return re.match(pattern, description)

    def get_description(self):
        description = input("description :")
        if self.is_valid_description(description):
            return description
        return self.get_description()


