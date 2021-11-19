from Tomato import Tomato
from TomatoBush import TomatoBush


class Gardener:

    @staticmethod
    def knowledge_base():
        print('Three types of tomato ripeness:\n'
              '1. Green tomato\n'
              '2. Yellow tomato\n'
              '3. Red tomato\n')

    def __init__(self, name: str):

        self.name = name

    def work(self, tomato: Tomato):
        tomato.grow()

    def harvest(self, tomatoBush: TomatoBush):

        if tomatoBush.all_are_ripe():
            tomatoBush.give_away_all()
            print('The harvest is harvested')
        else:
            print('Not all tomatoes are ripe')
