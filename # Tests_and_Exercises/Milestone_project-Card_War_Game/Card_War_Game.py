
#? =============================================================================
#* Milestone project - Card War Game
#? =============================================================================

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        print(f"{self.rank} of {self.suit}")
    
c1 = Card("Hearts", "Five")
card1 = c1

print(card1)