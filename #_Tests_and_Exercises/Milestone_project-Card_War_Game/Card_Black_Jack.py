
#? =============================================================================
#* Milestone Project - Card Game: Black Jack
#? =============================================================================
"""
- Blackjack cardgame with Computer Dealer
- Player has a starting budget of 10000 Credit (CR)
- NO INSURANCE, NO SPLIT, NO DOUBLE DOWN
- FIX BET >>> changed to betting system
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

#* Starting bet
bet = 100
#* Starting pot
pot = 0

    
# ==============================================================================
#* CARDS
# ==============================================================================

class Card():
    
    def __init__(self, rank, suit):
        
        self.suit = suit
        self.rank = rank
        self.value = card_values[rank]
        self.counted = False
        
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
        self.player_score = 0
        self.aces = 0
        
    def __str__(self) -> str:
        return f"\nPlayer Name: {self.playername}\nPlayer Balance:{self.balance} CR"
    
    def draw_one(self):
        return self.game_deck.fulldeck.pop()
    
    #* GAME COUNT | LOGIC
    def count_player_score(self):
        counter = 0
        for x in self.hand:
            #* ACES
            if x.value == 11 and x.counted == False :
                self.aces += 1
                if self.aces > 1:
                    x.value -= 10
                x.counted = True
            
            counter += x.value
        
        #* CHECKING ACES IF BUST    
        if counter > 21 and self.aces > 0:
            for x in self.hand:
                if x.value == 11 and x.counted == True:
                    x.value -= 10
                    counter -= 10
                else:
                    pass
                
        self.player_score = counter
        # return self.player_score

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
# test_player.player_score = test_player.show_counter()
# print(test_player.player_score)

# test_player.hand.append(test_player.draw_one())
# for x in test_player.hand:
#     print(x)
# test_player.player_score = test_player.show_counter()
# print(test_player.player_score)

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
    printBoard.append(f"                | {dealer.player_score} |                >>>{dealer.playername}")
    printBoard.append("----------------------------------------")
    printBoard.append(f"                | {player.player_score} |                >>>{player.playername}")
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
    print(f"                | {dealer.player_score} |                >>>{dealer.playername}")
    print(f"-----------------------------------------Bet: {bet} | Pot: {pot}")
    print(f"                | {player.player_score} |                >>>{player.playername}")
    print(f"                ------                >>>Balance: {player.balance} CR")
    print(f"            {player.hand[0]}                   ")
    print(f"            {player.hand[1]}                   ")
    
def printing_Board_extra():
    clear()
    
    for line in reversed(pulled_by_dealer):
        print(line)
        
    printing_Board(dealer, player1)
    
    for line in pulled_by_player:
        print(line)

def menu():
        print("\nChoose your action!")
        print("1. Draw a CARD!")
        print("2. Stop. Let's see the dealer's hand!")
        print("3. Bet!")
        
        print("")
        print("5. Quit the GAME")
        
        print(f"P1 aces: {player1.aces}")
        print(f"D aces: {dealer.aces}")

def menu_choose():
    menu_number = [1,2,3,5]
    while True:
        try:
            user_choice = int(input("Provide your action's number: "))
        except:
            print("That's not a number!")
            continue
        if (user_choice not in menu_number):
            print("That not a menu number! Try: 1,2,5 instead")
        else:
            break
    return user_choice

def check_win_condition(dealer:Player, player:Player):
    if player.player_score > 21:
        print("Player : BUST!")
        print("Dealer WON!")
    elif dealer.player_score > 21:
        print("Dealer : BUST!")
        print("Player WON!")
    elif dealer.player_score == player.player_score == 21:
        if len(dealer.hand) > len(player.hand):
            print("Draw but player has 21 with less card: Player1 WON!")
        elif len(dealer.hand) < len(player.hand):
            print("Draw but dealer has 21 with less card: Dealer WON!")
        elif len(dealer.hand) == len(player.hand):
            print("Draw!!! Player and Dealer has 21 with the same ammount of cards!")
    elif player.player_score < 21 and dealer.player_score < 21:
        if player.player_score > dealer.player_score:
            print("Player WON!")
    
def menu_Bet():
    print(f"<<<Current bet:{bet}>>>")
    print("\nChoose your action!")
    print("1. Enter YOUR bet!")
    print("2. Set MAXIMUM! (your are putting all of your credits in...)")
    print("")
    print("5. Back to the GAME")
            
def menu_Bet_choose():
    menu_number = [1,2,5]
    while True:
        try:
            user_choice = int(input("Provide your action's number: "))
        except:
            print("That's not a number!")
            continue
        if (user_choice not in menu_number):
            print("That not a menu number! Try: 1,2,5 instead")
        else:
            break
    return user_choice

def Bet(dealer:Player, player:Player, user_choice_bet:int):
    #* User enter a bet
    if user_choice_bet == 1:
        while True:
            try:
                entered_bet = int(input("Enter your bet: "))
            except:
                print("That's not a number!")
                continue
            if entered_bet > dealer.balance and entered_bet > player.balance:
                print(f"Thats more than Both of Your and the Dealer's balance. Maximum you can enter: {min(dealer.balance, player.balance)}")
            elif entered_bet > dealer.balance:
                print(f"Thats more than the Dealer's balance. Maximum you can enter: {dealer.balance}")
            elif entered_bet > player.balance:
                print(f"Thats more than Your balance. Maximum you can enter: {dealer.balance}")
            else:
                break
        return entered_bet
    
    #* User is all-in
    elif user_choice_bet == 2:
        return player.balance
    
    #* Return back to the game
    elif user_choice_bet == 5:
        printing_Board_extra()
        menu()
        user_choice = menu_choose()
    else:
        #* never can happen
        pass
    
def score(dealer:Player, player:Player, pot):
    if player.player_score <= 21 and dealer.player_score <= 21:
        if dealer.player_score > player.player_score:
            dealer.balance += pot
        elif dealer.player_score < player.player_score:
            player.balance += pot
        elif dealer.player_score == player.player_score:
            dealer.balance += pot/2
            player.balance += pot/2
            
    elif player.player_score > 21:
        if dealer.player_score <= 21:
            dealer.balance += pot
        else:
            dealer.balance += pot/2
            player.balance += pot/2
            
    elif dealer.player_score > 21:
        if player.player_score <= 21:
            player.balance += pot
        else:
            dealer.balance += pot/2
            player.balance += pot/2
    #* EMPTY THE POT
    pot = 0

def placing_Bets (dealer:Player, player:Player, bet):
    pass

# ==============================================================================
#* GAME BEGINS
# ==============================================================================
#* test START
# clear()
# game_deck = Deck()
# game_deck.shuffle_the_deck()

# player1 = Player("Zsolt", game_deck, 1_000)
# dealer = Player("Dealer", game_deck, 1_000_000)

# dealer.hand.append(dealer.draw_one())
# player1.hand.append(player1.draw_one())
# dealer.hand.append(dealer.draw_one())
# player1.hand.append(player1.draw_one())



# for x in player1.hand:
#     print(x)
# player1.count_player_score()
# print(player1.player_score)
# player1.hand.append(player1.draw_one())

# for x in player1.hand:
#     print(x)
# player1.count_player_score()
# print(player1.player_score)
#* test END

game_running = True

while game_running:
    clear()
    #* GENERATING THE DECK
    game_deck = Deck()
    game_deck.shuffle_the_deck()
    
    #* GENERATING THE PLAYERS
    player1 = Player("Zsolt", game_deck, 1_000)
    dealer = Player("Dealer", game_deck, 1_000_000)
    
    #* STORE NEW CARDS IN THESE FOR THE DISPLAY BOARD
    pulled_by_player = []
    pulled_by_dealer = []

    #*STARTING HANDS
    dealer.hand.append(dealer.draw_one())
    player1.hand.append(player1.draw_one())
    dealer.hand.append(dealer.draw_one())
    player1.hand.append(player1.draw_one())
    
    #*STARTING COUNTERS
    dealer.count_player_score()
    player1.count_player_score()
    
    #*STARTING BOARD
    printing_Board(dealer, player1)
    menu()
    user_choice = menu_choose()
    
    #*PLAYER CHOICES
    # while player1.player_score <= 21 or dealer.player_score <= 21:
    while user_choice != 5:
        if user_choice == 1:
            if player1.player_score <= 21:
                player1.hand.append(player1.draw_one())
                player1.count_player_score()
                
                #*output table
                printing_Board_extra()
                
                if player1.player_score > 21:
                    check_win_condition(dealer,player1)
                    break
                elif player1.player_score <= 21:
                    menu()
                    user_choice = menu_choose()
            else:
                check_win_condition(dealer, player1)
                break
        
        elif user_choice == 2:
            while (dealer.player_score <= 16) or (dealer.player_score <= player1.player_score):
                dealer.hand.append(dealer.draw_one())
                dealer.count_player_score()
                
                #*output table
                printing_Board_extra()
            else:
                check_win_condition(dealer, player1)
                break
            
        elif user_choice == 3:
            #*output table
            printing_Board_extra()
            menu_Bet()
            bet_choice = menu_Bet_choose()
            while bet_choice != 5:
                if bet_choice == 1:
                    bet = Bet(dealer, player1, bet_choice)
                    player1.balance -= bet
                    dealer.balance -= bet
                    pot = bet * 2
                elif bet_choice == 2:
                    bet = Bet(dealer, player1, bet_choice)
                    player1.balance -= bet
                    dealer.balance -= bet
                    pot = bet * 2
                else:
                    print("Wrong")
            if bet_choice == 5:
                bet = Bet(dealer, player1, bet_choice)
                player1.balance -= bet
                dealer.balance -= bet
                pot = bet * 2
            

            
            
        elif user_choice == 5:
            #*Quit the game
            break

    #* STOP RUNNING
    game_running = False