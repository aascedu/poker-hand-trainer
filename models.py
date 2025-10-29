#!/usr/bin/env python3

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
        random.shuffle(self.deck)
        random.shuffle(self.deck)
        random.shuffle(self.deck)

class Player():
    hand: tuple()
    position: int

    def __init__(self, max_pos: int):
        self.position = random.randint(0, max_pos - 1)

class Table():
    num_players: int
    deck: Deck
    player: Player

    def __init__(self, num_players: int):
        self.num_players = num_players
        self.deck = Deck()
        self.player = Player(self.num_players)

    def draw_hands(self):
        player_cards = []
        for i in range(self.num_players * 2):
            if i % self.num_players == self.player.position:
                player_cards.append(self.deck.deck[i])
            self.deck.deck.pop(i)
        self.player.hand = (player_cards[0], player_cards[1])
        player_cards.clear()

table = Table(random.randint(2, 5))
print(f"There are {table.num_players} players on this table.")
table.draw_hands()
print(table.player.hand)