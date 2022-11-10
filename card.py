class Card:
 suit= ["C","D","H","S"]
ranks= ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
def __init__(self, suit, rank):
                self.suit = suit
                self.rank = rank
def __str__(self) -> str:
            return self.suits[self.suit]+self.ranks[self.rank]
    
def __It__(self,other):
    if self.suit != other.suit:
        return self.suit < other.suit
    else:
        return self.rank < other.rank
