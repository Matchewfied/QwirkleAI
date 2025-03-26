import numpy as np
from collections import deque
DEFAULT_SEED = 22


class Deck:
    def __init__(self, contents: list, seed: int = DEFAULT_SEED, debug: bool = False):
        np.random.seed(seed)

        # Initialize deck and randomize its contents
        self.deck = deque(contents)
        if not debug:
            self.shuffle_()

    def get_size(self) -> int:
        return len(self.deck)

    def is_empty(self) -> bool:
        return self.get_size() == 0

    def shuffle_(self) -> None:
        np_deck = np.array(self.deck)
        np.random.shuffle(np_deck)
        self.deck = deque(np_deck)

    def draw_(self, num: int) -> list:
        drawn = []
        size = self.get_size()
        for i in range(min(num, size)):
            drawn.append(self.deck.pop())
        return drawn

    def place_(self, to_place: list, num: int = None) -> list:
        size = len(to_place) if num is not None else num
        remainder = to_place[size:]
        self.deck.extend(to_place[:size])
        return remainder

    def trade_(self, to_trade: list) -> list:
        drawn = self.draw_(len(to_trade))
        remainder = self.place_(to_trade, len(drawn))
        remainder.extend(drawn)

        return remainder

    def set_(self, contents: list) -> None:
        self.deck = deque(contents)

    def dg_listify_deck(self) -> list:
        return list(self.deck)
