from .Card import Card

class Hand():
    def __init__(self, fiveCards):
        self.cards = sorted(fiveCards, key=lambda x: x.rank)
        self.valueAsText = ""
        self.value = 0
        self.freqTable = self.returnFrequencyTable(self.cards)
        self.evaluate()

    def printHand(self):
        print(self.returnHandAndValue())

    def returnHandAndValue(self):
        result = ""
        for card in self.cards:
            result += card.asString()
            result += " "
        result = result.rstrip(' ')
        result += ", "
        result += self.valueAsText
        return result

    def evaluate(self):
        difCards = len(self.freqTable)

        if difCards == 2:
            if self.isFullHouse():
                self.valueAsText = "Full House"
            if self.isFourOfAKind():
                self.valueAsText = "Four of a kind"
        elif difCards == 3:
            if self.isThreeOfAKind():
                self.valueAsText = "Three of a kind"
            elif self.isTwoPair():
                self.valueAsText = "Two pairs"
        elif difCards == 4:
            if self.isOnePair():
                self.valueAsText = "One pair"
        elif difCards == 5:
            if self.isRoyalFlush():
                self.valueAsText = "Royal flush"
            elif self.isStraightFlush():
                self.valueAsText = "Straight flush"
            elif self.isFlush():
                self.valueAsText = "Flush"
            elif self.isStraight():
                self.valueAsText = "Straight"

        if not self.valueAsText:
            self.valueAsText = f"Highcard of {self.rankToCard(self.highCard())}"

    def rankToCard(self, rank):
        cards = {1:'A',
                 10: 'T',
                 11: 'J',
                 12: 'Q',
                 13: 'K',
                 14: 'A'}

        return cards.get(rank, rank)

    def highCard(self):
        #Edgecase of A = 14 or 1
        if self.cards[0].rank == 1:
            return 14
        return self.cards[-1].rank

    def isOnePair(self):
        # if length of dictionary is 4 there are 2 of same and 3 different cards.
        return len(self.freqTable) == 4


    def isTwoPair(self):
        # Lenght of dictionary should be 3 since only cards with three different ranks appear. Check permutation is [1, 1, 2]
        frequencies = self.SortedFreqListFromTable(3)

        if len(self.freqTable) == 3 and frequencies == [1,2,2]:
            return True

        return False

    def isThreeOfAKind(self):
        # Lenght of dictionary should be 3 since only cards with three different ranks appear. Check permutation is [1, 1, 3]
        frequencies = self.SortedFreqListFromTable(3)

        return len(self.freqTable) == 3 and frequencies == [1, 1, 3]


    def isStraight(self):
        # Edgecase of TJQKA
        if self.cards[0].rank == 1 and self.cards[1].rank == 10:
            for j in range(1, len(self.cards)-1):
                if self.cards[j].rank != self.cards[j + 1].rank - 1:
                    return False
            return True

        for i in range(len(self.cards)-1):
            if self.cards[i].rank != self.cards[i+1].rank-1:
                return False
        return True

    def isFlush(self):
        suit = self.cards[0].suit
        return all([card.suit == suit for card in self.cards])

    def isFullHouse(self):
        # Length of dictionary should be 2 since only cards with two different ranks appear. Check permutation is [2, 3]
        frequencies = self.SortedFreqListFromTable(2)

        return len(self.freqTable) == 2 and frequencies == [2, 3]

    def isFourOfAKind(self):
        #Length of dictionary should be 2 since only cards with two different ranks appear. Check permutations of [1, 4]
        frequencies = self.SortedFreqListFromTable(2)

        return len(self.freqTable) == 2 and frequencies == [1, 4]

    def isStraightFlush(self):
        return self.isStraight() and self.isFlush()

    def isRoyalFlush(self):
        #Edgecase of A2345 of same suit.
        if self.cards[2].rank < 10:
            return False

        return self.isStraight() and self.isFlush() and self.highCard() == 14

    def returnFrequencyTable(self, cards):
        dict = {}
        # Frequency table with card rank as key and how many times it shows up as value
        for card in cards:
            if card.rank in dict:
                dict[card.rank] += 1
            else:
                dict[card.rank] = 1
        return dict

    def SortedFreqListFromTable(self, howMany):
        cardFreqIterator = iter(self.freqTable.values())
        values = [next(cardFreqIterator) for i in range(howMany)]

        return sorted(values)


