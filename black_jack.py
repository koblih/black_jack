import random

suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
ranks = ['A',1,2,3,4,5,6,7,8,9,10,'J','Q','K']

class Card(object):

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.card = [self.rank, self.suit]  

    def __repr__(self):
                     
        return str(self.card)

# to be able to get the value of the card
    def __getitem__(self, key):
        return self.card[key]

class Deck(object):
       
    def __init__(self):
        self.deck = []
        self.create_deck()

# create deck using hard coded values of cards

    def create_deck(self):       
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))
        
    def __repr__(self):
        return 'The current deck contains: {}'.format(self.deck)

# hand class to calculate the value of the hand and display cards
# make Hand subclass of deck

class Hand(Deck):

    def __init__(self):
        Deck.__init__(self)
        self.hand = [] 
        self.hand_value = 0

# selecting a random card from the deck 

    def get_card(self):
        selection = random.choice(self.deck)
        self.hand.insert(0,selection)
        print 'Your hand: {}'.format(self.hand)

# testing of hand value loop

#    def test_card_value(self):
#        selection = Card('A', 'Hearts')
#        self.hand.append(selection)
#        print '{}'.format(self.hand)

# get value of the randomly selected card and add it to the hand value

    def get_value(self):
        card_value = self.hand[0][0]
        if card_value in range(1,10):
            self.hand_value += card_value
        elif (card_value == 'J' or card_value == 'Q' or card_value == 'K'):
            self.hand_value += 10
        else:
            if self.hand_value < 12:
                self.hand_value += 10
            else:
                self.hand_value += 1
        print '{}'.format(self.hand_value)

def main():
    
    hand = Hand()
    hand.get_card()
#    hand.test_card_value()
    hand.get_value()
    hand.get_card()
    hand.get_value()
    hand.get_card()
    hand.get_value()
    
main()
