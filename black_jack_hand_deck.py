import random

suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
ranks = ['A',1,2,3,4,5,6,7,8,9,10,'J','Q','K']

# card class to create a card and get its value

class Card(object):

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return '{} of {}'.format(self.rank, self.suit)
		
# deck class to create the deck of cards and deal from it?

class Deck(object):
       
    # the below list of tuples potentially to be list of dictionaries
    def __init__(self):
        self.deck = []
        self.create_deck()
       
    def create_deck(self):       
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
        
    def __repr__(self):
        return 'The current deck contains: {}'.format(self.deck)

# hand class to calculate the value of the hand and display cards
# make Hand subclass of deck?

class Hand(Deck):

    def __init__(self):
        self.hand = [] 
        self.value = 0

    def get_card(self, Deck):
        self.selection = random.choice(self.deck)
        print 'This is your card: {}'.format(self.selection)

#    def get_value(self):


def main():

    card = Card('ace', 'hearts')
    print card

    deck = Deck()
    print deck

    hand = Hand()
    hand.get_card(deck)

        
main()
