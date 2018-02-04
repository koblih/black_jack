import random

suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
ranks = ['A',1,2,3,4,5,6,7,8,9,10,'J','Q','K']

# card class to create a card and get its value

class Card(object):

    def __init__(self, suit, rank):
	    self.suit = suit
	    self.rank = rank

    def __str__(self):
        return '{} of {}'.format(self.suit, self.rank)
		
# deck class to create the deck of cards and deal from it?

class Deck(object):
       
    # the below list of tuples potentially to be list of dictionaries
    def __init__(self, deck = []):
        self.deck = deck
        for suit in suits:
            for rank in ranks:
                self.deck.append((suit, rank))
        
    def __str__(self):
        return 'the deck is {}'.format(self.deck)

# hand class to calculate the value of the hand and display cards

#class Hand(object):

#    def __init__(self):
#        hand = [] 
        
#    def get_card

    #def select_card(self, deck):
        #selected_card = random.choice(deck)
        #print selected_card

def main():

    card = Card('ace', 'hearts')
    print card

    deck = Deck()
    print deck

#    hand = Hand
#    print hand


        
main()
