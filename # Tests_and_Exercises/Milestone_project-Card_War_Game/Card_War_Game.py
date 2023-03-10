
#? =============================================================================
#* Milestone project - Card War Game
#? =============================================================================
import random

#* GLOBALS:

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

class Deck():
    
    def __init__(self,):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
                
new_deck = Deck()
print(new_deck.all_cards)

first_card = new_deck.all_cards[0]
print(first_card)
new_deck.shuffle()

for card in new_deck.all_cards:
    print(card)
    