
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
import os

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

printBoard = []


    
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
                created_card = Card(rank, suit)
                self.fulldeck.append(created_card)
                
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
# for x in myDeck.fulldeck:
#     print(x)
# myDeck.shuffle_the_deck()
# myDeck.list_the_deck()

# ==============================================================================
#* PLAYERS
# ==============================================================================

class Player():
    
    def __init__(self, player_name:str, game_deck:Deck, balance:int):
        
        self.playername = player_name
        self.game_deck = game_deck
        self.balance = balance
        self.hand = []
        self.hand_counter = 0
        
    def __str__(self) -> str:
        return f"\nPlayer Name: {self.playername}\nPlayer Balance:{self.balance} CR"
    
    def draw_one(self):
        return self.game_deck.fulldeck.pop()
    
    def show_counter(self):
        counter = 0
        for x in self.hand:
            counter += x.value
        self.hand_counter = counter
        return self.hand_counter

test_deck = Deck()
test_deck.shuffle_the_deck()
"""
* Max length
len_deck = []
for x in test_deck.fulldeck:
    len_deck.append(len(str(x)))
print(max(len_deck))
* 17 char is the max
"""
# test_player = Player("Zsolt", test_deck, 10000)
# print(test_player)

# test_player.hand.append(test_player.draw_one())
# test_player.hand.append(test_player.draw_one())

# for x in test_player.hand:
#     print(x)
# test_player.hand_counter = test_player.show_counter()
# print(test_player.hand_counter)

# test_player.hand.append(test_player.draw_one())
# for x in test_player.hand:
#     print(x)
# test_player.hand_counter = test_player.show_counter()
# print(test_player.hand_counter)

# ==============================================================================
#* FUNCTIONS
# ==============================================================================
def clear():
    os.system("cls")
    
#* List version
def load_printBoard(dealer:Player, player:Player):
    printBoard.append(f"            {dealer.hand[1]}                   ")
    printBoard.append(f"            {dealer.hand[0]}                   ")
    printBoard.append(f"                ------                >>>Balance: {dealer.balance} CR")
    printBoard.append(f"                | {dealer.hand_counter} |                >>>{dealer.playername}")
    printBoard.append("----------------------------------------")
    printBoard.append(f"                | {player.hand_counter} |                >>>{player.playername}")
    printBoard.append(f"                ------                >>>Balance: {player.balance} CR")
    printBoard.append(f"            {player.hand[0]}                   ")
    printBoard.append(f"            {player.hand[1]}                   ")
    

def print_the_Board():
    for item in printBoard:
        print(item)

#* Print version        
def printing_Board(dealer:Player, player:Player):
    print(f"            {dealer.hand[1]}                   ")
    print(f"            {dealer.hand[0]}                   ")
    print(f"                ------                >>>Balance: {dealer.balance} CR")
    print(f"                | {dealer.hand_counter} |                >>>{dealer.playername}")
    print("----------------------------------------")
    print(f"                | {player.hand_counter} |                >>>{player.playername}")
    print(f"                ------                >>>Balance: {player.balance} CR")
    print(f"            {player.hand[0]}                   ")
    print(f"            {player.hand[1]}                   ")

def menu() -> int:
        print("\nChoose your action!")
        print("1. Draw a CARD!")
        print("2. Stop. Let's see the dealer's hand!")
        print("")
        print("5. Quit the GAME")
        
        menu = [1,2,5]
        while True:
            try:
                user_choice = int(input("Provide your action's number: "))
            except:
                print("That's not a number!")
                continue
            if (user_choice not in menu):
                print("That not a menu number! Try: 1,2,5 instead")
            else:
                break
        return user_choice
    
def check_win_condition(dealer:Player, player:Player):
    if player.hand_counter > 21:
        print("Player1 : BUST!")
        print("Dealer WON!")
    elif dealer.hand_counter > 21:
        print("Dealer : BUST!")
        print("Player WON!")
    elif dealer.hand_counter == player.hand_counter == 21:
        if len(dealer.hand) > len(player.hand):
            print("Draw but player has 21 with less card: Player1 WON!")
        elif len(dealer.hand) < len(player.hand):
            print("Draw but dealer has 21 with less card: Dealer WON!")
        elif len(dealer.hand) == len(player.hand):
            print("Draw!!! Player and Dealer has 21 with the same ammount of cards!")
    elif player.hand_counter < 21 and dealer.hand_counter < 21:
        if player.hand_counter > dealer.hand_counter:
            print("Player1 WON!")
        
# ==============================================================================
#* GAME LOGIC
# ==============================================================================

game_running = True

while game_running:
    clear()
    #* GENERATING THE DECK
    game_deck = Deck()
    game_deck.shuffle_the_deck()
    
    #* GENERATING THE PLAYERS
    player1 = Player("Zsolt", game_deck, 1_000)
    dealer = Player("Dealer", game_deck, 1_000_000)
    
    pulled_by_player = []
    pulled_by_dealer = []

    #*STARTING HANDS
    dealer.hand.append(dealer.draw_one())
    player1.hand.append(player1.draw_one())
    dealer.hand.append(dealer.draw_one())
    player1.hand.append(player1.draw_one())
    
    #*STARTING COUNTERS
    dealer.show_counter()
    player1.show_counter()
        
    printing_Board(dealer, player1)
    user_choice = menu()
    
    #*PLAYER CHOICES
    # while player1.hand_counter <= 21 or dealer.hand_counter <= 21:
    while user_choice != 5 or player1.hand_counter <= 21 or dealer.hand_counter <= 21:
        if user_choice == 1:
            player1.hand.append(player1.draw_one())
            player1.show_counter()
            clear()
            pulled_by_player.append(f"            {player1.hand[-1]}                   ")
            for line in reversed(pulled_by_dealer):
                print(line)
            printing_Board(dealer, player1)
            for line in pulled_by_player:
                print(line)
            user_choice = menu()
        
        elif user_choice == 2:
            while (dealer.hand_counter <= 16) or (dealer.hand_counter <= player1.hand_counter):
                dealer.hand.append(dealer.draw_one())
                dealer.show_counter()
                clear()
                pulled_by_dealer.append(f"            {dealer.hand[-1]}                   ")
                for line in reversed(pulled_by_dealer):
                    print(line)
                printing_Board(dealer, player1)
                for line in pulled_by_player:
                    print(line)
            user_choice = menu()
            
        elif user_choice == 5:
            break

    #* STOP RUNNING
    game_running = False

