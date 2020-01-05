class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return '{} of {}'.format(self.value, self.suit )

class Deck:
    card_remains = 52

    #

    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(value, suit) for suit in suits for value in values]
        print(self.cards)

    def count(self):
        return len(self.cards)
        # self.cards = [(suit, value) for suit in suits for value in values]
        # print(self.cards)

    def _deal(self, num):
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        # 'actual' cards from cards to be removed - actually we get it to return
        self.cards = self.cards[:-actual]
        # adjust the cards & remove 'actual' cards
        return cards

d = Deck()
print(d._deal(52))
print(d.count())
print(d._deal(3))
