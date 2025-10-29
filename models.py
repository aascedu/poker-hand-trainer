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

class Hand():
    cards: tuple()

    def __init__(self, first_card: str, second_card: str):
        self.cards = tuple(first_card, second_card)

class Player():
    hand: Hand
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
        print(self.player.position)
        for i in range(self.num_players * 2):
            if i % self.num_players == self.player.position:
                print(f"Player {self.player.position} got {self.deck.deck[i]}")


table = Table(3)
table.draw_hands()
