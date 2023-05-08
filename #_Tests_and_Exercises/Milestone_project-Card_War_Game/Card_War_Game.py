
#? =============================================================================
#* Milestone project - Card War Game
#? =============================================================================
import random

# ==============================================================================
#* GLOBALS
# ==============================================================================

suits = ("Hearts",
        "Clubs",
        "Spades",
        "Diamonds")

ranks = ("Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Jack",
        "Queen",
        "King",
        "Ace")

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
    "Jack" : 11,
    "Queen" : 12,
    "King" : 13,
    "Ace" : 14
}

# ==============================================================================
#* CARD CLASS
# ==============================================================================

class Card():

    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = card_values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
c1 = Card("Hearts", "Five")

print(c1)
print(c1.rank)
print(c1.value)

three_of_hearts = Card("Hearts", "Three")
print(three_of_hearts)
print(three_of_hearts.value)
print(three_of_hearts.suit)

# ==============================================================================
#* DECK CLASS
# ==============================================================================

class Deck():
    
    def __init__(self,):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()
                
new_deck = Deck()
print(new_deck.all_cards)

first_card = new_deck.all_cards[0]
print(first_card)
new_deck.shuffle()

for card in new_deck.all_cards:
    print(card)

popped_ones = []

for i in range(10):
    popped_ones.append(new_deck.deal_one())

print("\nCards we popped out:\n")    
for c in popped_ones:
    print(c)

print("\nCards left in the deck:")    
print(f"Number of cards left: {(len(new_deck.all_cards))}\n")
for c in new_deck.all_cards:
    print(c)
print("\n")
# ==============================================================================
#* PLAYER CLASS
# ==============================================================================

class Player():
    
    def __init__ (self, name):
        
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type( [] ):
            #* List of multiple card obj
            self.all_cards.extend(new_cards)
        else:
            #* List of single card obj
            self.all_cards.append(new_cards)
    
    def __str__(self) -> str:
        return f"Player {self.name} has {len(self.all_cards)} cards."

deck1 = Deck()
deck1.shuffle()
my_card = deck1.deal_one()
print(f"My card: {my_card}")
    
new_player = Player("Zsolt")
print(new_player)

new_player.add_cards(my_card)
print(new_player)

new_player.add_cards([my_card, my_card, my_card])
print(new_player)

new_player.remove_one()
print(new_player)

for card in new_player.all_cards:
    print(card)