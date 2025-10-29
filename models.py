#!/usr/bin/env python3

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
    community: tuple

    def __init__(self, num_players: int):
        self.num_players = num_players
        self.deck = Deck()
        self.player = Player(self.num_players)
        self.community = ()

    def draw_hands(self):
        player_cards = []
        for i in range(self.num_players * 2):
            if i % self.num_players == self.player.position:
                player_cards.append(self.deck.deck[0])
            self.deck.deck.pop(0)
        self.player.hand = (player_cards[0], player_cards[1])
        player_cards.clear()

    def draw_flop(self):
        for i in range(4):
            if i != 0:
                self.community = self.community + (self.deck.deck[0], )
            self.deck.deck.pop(0)
        print(self.community)


def main():
    table = Table(3)
    print(f"There are {table.num_players} players on this table, you are {table.player.position + 1}rd to play.")
    table.draw_hands()
    print(table.player.hand)
    table.draw_flop()

if __name__ == "__main__":
    main()