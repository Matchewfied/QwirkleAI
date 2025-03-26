import numpy as np

DEFAULT_SEED = 22


class Qwirkle:

    def __init__(self, num_players: int, num_ai: int, seed: int = DEFAULT_SEED):
        """
        num_players: the number of players that will be in the game (2-4)
        num_ai: the number of players that will be computers (num_ai <= num_players)
        """
        np.random.seed(seed)

        # Initialize the deck, tiles are represented as integers from 0 to 35
        self.deck = np.array([i for i in range(36) for _ in range(3)])
        self.shuffle_deck()


        self.hands = {}
        for i in range(num_players):

    def

    def shuffle_deck(self) -> bool:
        if self.deck.size > 0:
            np.random.shuffle(self.deck)
            return True
        return False

    def draw(self, num) -> np.array
        drawn = self.deck[-num:]
        self.deck = []

