import random

suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
ranks = ['A',1,2,3,4,5,6,7,8,9,10,'J','Q','K']

class Card(object):

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
                     
        return '{} of {}'.format(self.rank, self.suit)
		
class Deck(object):
       
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
# make Hand subclass of deck

class Hand(Deck):

    def __init__(self):
        Deck.__init__(self)
        self.hand = [] 
        self.hand_value = 0

    def get_card(self):
        selection = random.choice(self.deck)
        self.hand.append(selection)
        print 'Your hand: {}'.format(self.hand)

# get value of the randomly selected card and add it to the hand value
# decompose self.hand to get self.rank out of it then loop out its value
    def get_value(self):
        print self.hand        


def main():
    
    card = Card('ace', 'hearts')
    print card

    deck = Deck()
    print deck

    hand = Hand()
    hand.get_card()
    hand.get_value()

        
main()
