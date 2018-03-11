import random

suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
ranks = ['A',1,2,3,4,5,6,7,8,9,10,'J','Q','K']

# card as a list of two values

class Card(object):

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.card = [self.rank, self.suit]  

    def __repr__(self):
        return str(self.card)

# to be able to get the value of the card - make iterable
    def __getitem__(self, key):
        return self.card[key]

# deck as list of lists

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
        self.deck.remove(selection)
        print 'Your hand: {}'.format(self.hand)

# get value of the randomly selected card and add it to the hand value
# this means getting the first [0] item of the card list selected randomly from the deck list and appended to the hand list
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
  

# create two hands for each player (for now one pleayer against computer)
# maybe ask how many players will play?
# ask the players to put the names in
# after the names are in deal two cards to each player
# ask one by one if they want another card to be dealt (note this way the other players will always know the hand value of other players)
# display the hand and the hand value
# depending on hand value ask if they want more, or tell them they are bust
# calculate if there is a winner and display the relevant message

def main():

    deck = Deck()

    while True:
        no_of_players = raw_input('Please enter the number of players: ')
        if not no_of_players.isdigit():
            print 'Please enter the NUMBER of players! '
            continue
        else:
            pass



main()    
