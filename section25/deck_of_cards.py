from random import shuffle

class Card:
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self, suit, value):                
        self.suit = suit        
        self.value = value
    
    def __repr__(self):
        return f"{value} of {suit}"

class Deck:
    def __init__(self):
        cards = []        
        for suit in Card.suits:
            for value in Card.values:
                cards.append(Card(suit, value))
        
    def __repr__(self):
        return f"Deck of {count()} cards"
    
    def _deal(self, num):
        if count() == 0:
            return ValueError("All cards have been dealt")
        elif num > count():
            num = count()
        
        for val in range(0, num):
            self.cards.pop()
    
    def count(self):
        return len(self.cards)

    
        
