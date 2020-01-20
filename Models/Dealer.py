from .Hand import Hand
from .Card import Card
import random

class Dealer():
    def __init__(self, players = 3):
        self.data = 0
        self.players = players

    def generateDeck(self):
        deckOfCards = []
        suits = ['d', 'c', 'h', 's']
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suits[suit], rank)
                deckOfCards.append(card)

        random.shuffle(deckOfCards)
        return deckOfCards

    def dealToPlayers(self):
        hands = self.dealXHands(self.players)
        with open('analysis.txt', 'w') as file:
            for i in range(self.players):
                print(f"Player {i+1} has:")
                hands[i].printHand()
                file.write(hands[i].returnHandAndValue())
                file.write('\n')

    def dealXHands(self, x):
        if x > 10:
            print('not enough cards in deck')
        deck = self.generateDeck()
        hands = []
        for hand in range(x):
            listOfCards = [deck.pop(0) for card in range(5)]
            hand = Hand(listOfCards)
            hands.append(hand)

        return hands

    def frequencyTableOfHandDistribution(self, millionHands):
        print("Generating...")
        frequencyTable = {}
        totalHands = millionHands*100000
        progressBar = 0
        for i in range(totalHands):
            if i % (totalHands/10) == 0:
                progressBar += 10
                print(f"{progressBar}%")
            hands = self.dealXHands(10)
            for hand in hands:
                if hand.valueAsText in frequencyTable:
                    frequencyTable[hand.valueAsText] += 1
                else:
                    frequencyTable[hand.valueAsText] = 1

        totalAmountOfValues = 0
        for key in frequencyTable:
            totalAmountOfValues += frequencyTable[key]

        for key in frequencyTable:
            frequencyTable[key] = ((frequencyTable[key] / totalAmountOfValues) * 100)

        with open('frequencies.txt', 'w') as file:
            for i in sorted(frequencyTable):
                print(i,":", frequencyTable[i],"%")
                file.write(f"{i}: {frequencyTable[i]}%")
                file.write("\n")

            prtTotalHands = f"{totalAmountOfValues/1000000} Million hands" if totalAmountOfValues >= 1000000 else f"{totalAmountOfValues} Hands"
            print(prtTotalHands)
            file.write(prtTotalHands)

