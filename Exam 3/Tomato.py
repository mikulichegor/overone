class Tomato:

    states = {1: 'Green tomato',
              2: 'Yellow tomato',
              3: 'Red tomato'}

    def __init__(self, index: int):

        self._index = index
        self._state = Tomato.states[1]

    def grow(self):

        self._state = Tomato.states[2] if self._state == Tomato.states[1] else Tomato.states[3]

    def is_ripe(self) -> bool:

        return True if self._state == Tomato.states[3] else False

    def show_ripe(self):
        return self._state
