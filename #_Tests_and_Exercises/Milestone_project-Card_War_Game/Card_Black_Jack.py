
#? =============================================================================
#* Milestone Project - Card Game: Black Jack
#? =============================================================================
"""
- Blackjack cardgame with Computer Dealer
- Player has a starting budget of 10000 Credit (CR)
- NO INSURANCE, NO SPLIT, NO DOUBLE DOWN
- FIX BET
"""
# ==============================================================================
#* IMPORTS
# ==============================================================================
import random

# ==============================================================================
#* DECLARATION AND INITIALIZATION
# ==============================================================================

suits = ["Hearts","Clubs","Diamonds","Spades"]

ranks = ["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]

card_values = {
    "Two" : 2,
    "Three" : 3, 
    "Four" : 4,
    "Five" : 5,
    "Six" : 6,
    "Seven" : 7,
    "Eight" : 8, 
    "Nine" : 9, 
    "Ten" : 10,
    "Jack" : 10,
    "Queen" : 10,
    "King" : 10,
    "Ace" : 11
}


# ==============================================================================
#* CARDS
# ==============================================================================

class Card():
    
    def __init__(self, rank, suit):
        
        self.suit = suit
        self.rank = rank
        self.value = card_values[rank]
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"
        
testCard = Card("Ace","Spades")
# print(testCard)

# ==============================================================================
#* DECKS
# ==============================================================================

class Deck():
    
    def __init__(self):
        
        self.fulldeck = []
        
        for suit in suits:
            for rank in ranks:
                self.fulldeck.append(Card(rank, suit))
                
    def __str__(self) -> str:
        return f"This deck has {len(self.fulldeck)} cards in it"
    
    def list_the_deck(self):
        for card in self.fulldeck:
            print(card)
            
    def shuffle_the_deck(self):
        random.shuffle(self.fulldeck)

#*Test the deck        
# myDeck = Deck()
# print(myDeck)
# myDeck.shuffle_the_deck()
# myDeck.list_the_deck()

# ==============================================================================
#* HANDS
# ==============================================================================

class Hand():
    
    def __init__(self):
        
        
        pass



# ==============================================================================
#* PLAYER
# ==============================================================================

class Player():
    
    def __init__(self, player_name, balance):
        
        self.playername = player_name
        self.balance = balance
        
    def __str__(self) -> str:
        return f"\nPlayer Name: {self.playername}\nPlayer Balance:{self.balance} CR"
    
zsolt = Player("Zsolt", 10000)
zsolt.player_deck.list_the_deck()
print(zsolt)