import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
        'Queen':10, 'King':10, 'Ace':11}

playing = True

#============================================================== Classes ==============================================================#

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))  # build Card objects and add them to the list
    
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
                self.aces += 1
    
    def ace_count(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

#============================================================== Methods ==============================================================#

def take_bet(chips):
    while True:
        
        try:
            chips.bet = int(input(f"How much would you like to bet? "))
        except ValueError:
            print("That isn't a number, please try again")
        else:
            if chips.bet > chips.total:
                print('You don\'t have enough chips! You have: {}'.format(chips.total))
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.ace_count()

def hit_or_stand(deck,hand):
    global playing
    
    while True:
        ask = input(f'Player has {hand.value}\nHit or Stand? Please enter \'h\' or \'s\': ')
        if ask[0].lower() == 'h':
            hit(deck,hand)
        elif ask[0].lower() == 's':
            print('\nPlayer stands!\nIt\'s the Dealer\'s Turn!')
            playing = False
        else:
            print('Sorry! Please Try Again! Enter \'h\' for hit, or \'s\' for stand')
            continue
        break

def show_some(player,dealer):
    print("\nDealer's hand:")
    print("\nFirst card hidden")
    print(dealer.cards[1])
    
    print("\nPlayer's hand:\n")
    for card in player.cards:
        print(card)
    
def show_all(player,dealer):
    print("Dealer's hand:\n")
    for card in dealer.cards:
        print(card)
    print(f"\nDealer's has {dealer.value}")
    
    print("\nPlayer's hand:\n")
    for card in player.cards:
        print(card)
    print(f"\nPlayer's has {player.value}")

def player_busts(player, dealer, chips):
    print(f'Player BUST! Dealer wins')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print(f'Player wins!')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    player.value > 21
    print(f'Dealer BUST! Player wins')
    chips.win_bet()
    
def dealer_wins(player, dealer, chips):
    print(f'Dealer wins!')
    chips.lose_bet()
    
def push(player, dealer):
    print('It\'s a tie! Push!')

#============================================================== Game ==============================================================#