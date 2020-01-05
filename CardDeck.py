from random import shuffle

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return '{} of {}'.format(self.value, self.suit )

class Deck:
    card_remains = 52

    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(value, suit) for suit in suits for value in values]
        print(self.cards)

    def __repr__(self):
        return 'Deck of {} cards'.format(self.count())

    def count(self):
        return len(self.cards)

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

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        # return self
        # conventional if we want to save it to a variable

    def deal_card(self):
        return self._deal(1)[0]
        # Nếu không có [0] nó sẽ trả về 1 list v 1 element in it


    def deal_hand(self, hand_size):
        return self._deal(hand_size)
