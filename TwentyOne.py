# -*- coding: utf-8 -*-
import random


SUITS = ('♥','♦','♠','♣')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7,
          '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print ("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank


class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):

        result = ""
        for card in self.cards:
            result += " " + card.__str__()

        return "Hand contains" + result

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        contains_ace = False

        for card in self.cards:
            rank = card.get_rank()
            value += VALUES[rank]

            if(rank == 'A'):
                contains_ace = True

        if(value < 11 and contains_ace):
            value += 10

        return value


class Deck:
    def __init__(self):
        self.cards = []

        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)


def player(player_hand):
    if player_hand.get_value() <= 21:
        take = raw_input("Do you want new card? Enter Yes if not press Enter:")
        if take.lower() == 'yes':
            player_hand.add_card(deck.deal_card())
            if player_hand.get_value() <= 21:
                print('Player score {}'.format(player_hand.get_value()))
                return player(player_hand)

    elif player_hand.get_value() > 21:
        print("You loose")
        return True


def dealer(dealer_hand):
    print('Dealer score {}'.format(dealer_hand.get_value()))
    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(deck.deal_card())

    print ("Dealer: %s" % dealer_hand)
    print('Dealer score {}'.format(dealer_hand.get_value()))
    print('Player score {}'.format(player_hand.get_value()))

    if dealer_hand.get_value() > 21:
        print ("Dealer is busted. Player wins.")
        return True
    else:
        if dealer_hand.get_value() >= player_hand.get_value() \
                or player_hand.get_value() > 21:
            print ("Dealer wins")
        else:
            print('Player score {}'.format(player_hand.get_value()))
            print("Player wins.")
        return True


def deal():
    global deck, player_hand, dealer_hand, deck

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())

    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

    print("Player: %s" % player_hand)
    print('Player score {}'.format(player_hand.get_value()))
    print("Dealer: %s" % dealer_hand)
    print('Dealer score {}'.format(dealer_hand.get_value()))


    while True:
        game_over = player(player_hand)
        if game_over:
            return

        game_over = dealer(dealer_hand)
        if game_over:
            return

deal()

