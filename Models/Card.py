class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def rankToCard(self, rank):
        cards = {1:"A",
                 10: 'T',
                 11: 'J',
                 12: 'Q',
                 13: 'K'}

        return cards.get(rank, rank)

    def asString(self):
        string = f"{self.rankToCard(self.rank)}{self.suit}"
        return string