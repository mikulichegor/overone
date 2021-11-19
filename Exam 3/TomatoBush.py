from Tomato import Tomato


class TomatoBush:

    def __init__(self, number: int):
        self.tomatoes = []
        for i in range(number):

            self.tomatoes.append(Tomato(i))

    def grow_all(self):

        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self):

        for i in self.tomatoes:
            if not i.is_ripe():
                return False
        return True

    def give_away_all(self):

        self.tomatoes.clear()
