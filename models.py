import itertools
import random

class Deck():
    COLOR = ('h', 'd', 'c', 's')
    CARDS = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
    deck: list[str]

    def __init__(self):
        self.deck = []
        for color in self.COLOR:
            for card in self.CARDS:
                self.deck.append(card + color)
        random.shuffle(self.deck)

class Hand():
    cards: tuple

class Table():
    num_players: int
    deck: Deck
    hands: list[Hand]

    def __init__(self, num_players: int):
        self.num_players = num_players
        self.deck = Deck()

    def draw_cards(self):
        pass


deck = Deck()
print(deck.deck)
