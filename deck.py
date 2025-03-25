import numpy as np
from collections import deque
DEFAULT_SEED = 22


class Deck:
    def __init__(self, contents: list, seed: int = DEFAULT_SEED, debug: bool = False):
        np.random.seed(seed)

        # Initialize deck and randomize its contents
        self.deck = deque(contents)
        if not debug:
            self._shuffle()

    def get_size(self) -> int:
        return len(self.deck)

    def is_empty(self) -> bool:
        return self.get_size() == 0

    def _shuffle(self) -> None:
        np_deck = np.array(self.deck)
        np.random.shuffle(np_deck)
        self.deck = deque(np_deck)

    def _draw(self, num: int) -> list:
        drawn = []
        size = self.get_size()
        for i in range(min(num, size)):
            drawn.append(self.deck.pop())
        return drawn

    def _place(self, to_place: list, num: int = None) -> list:
        size = len(to_place) if num is not None else num
        remainder = to_place[size:]
        self.deck.extend(to_place[:size])
        return remainder

    def _trade(self, to_trade: list) -> list:
        drawn = self._draw(len(to_trade))
        remainder = self._place(to_trade, len(drawn))
        remainder.extend(drawn)

        return remainder

    def _set(self, contents: list) -> None:
        self.deck = deque(contents)


    def dg_display_deck(self) -> None:
        print(self.deck)


    def dg_verify_contents(self, contents: list) -> None:
        deck_contents = list(self.deck)
        if deck_contents == contents:
            print("Contents verified successfully")
        else:
            print("Equality failed. Here is self.deck:")
            self.dg_display_deck()
            print("Here is contents input:")
            print(contents)
            ldc, lc = len(deck_contents), len(contents)
            if ldc != lc:
                print("Length is different, we have that len(deck_contents) - len(contents) is " + str(ldc - lc))
            for i in range(min(ldc, lc)):
                if deck_contents[i] != contents[i]:
                    print("First mismatch at index " + str(i))
                    print(str(deck_contents[i]) + " is not equal to " + str(contents[i]))
                    break







