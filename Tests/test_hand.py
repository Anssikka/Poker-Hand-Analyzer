import random

import pytest
from Models.Card import Card
from Models.Hand import Hand


class TestEvaluation:
    def test_highCard(self):
        ranks = [1, 2, 8, 4, 5]
        suits = ['d', 'c', 'h', 's', 'd']
        hand = Hand([Card(suits[i], ranks[i]) for i in range(5)])

        assert hand.valueAsText == "Highcard of A"


    def test_onePair(self):
        ranks = [1, 2, 2, 4, 5]
        suits = ['d', 'c', 'h', 's', 'd']
        hand = Hand([Card(suits[i], ranks[i]) for i in range(5)])

        assert hand.valueAsText == "One pair"

    def test_twoPair(self):
        ranks = [1, 2, 2, 4, 4]
        suits = ['d', 'c', 'h', 's', 'd']
        hand = Hand([Card(suits[i], ranks[i]) for i in range(5)])

        assert hand.valueAsText == "Two pairs"

    def test_threeOfAKind(self):
        ranks = [1, 3, 3, 3, 5]
        suits = ['d', 'c', 'h', 's', 'd']
        hand = Hand([Card(suits[i], ranks[i]) for i in range(5)])

        assert hand.valueAsText == "Three of a kind"

    def test_straight(self):
        ranks = [1, 2, 3, 4, 5]
        suits = ['d', 'c', 'h', 's', 'd']
        hand = Hand([Card(suits[i], ranks[i]) for i in range(5)])

        assert hand.valueAsText == "Straight"

    def test_flush(self):
        ranks = [1, 2, 7, 11, 5]
        suits = ['d', 'd', 'd', 'd', 'd']
        hand = Hand([Card(suits[i], ranks[i]) for i in range(5)])

        assert hand.valueAsText == "Flush"

    def test_fullHouse(self):
        ranks = [1, 1, 1, 5, 5]
        suits = ['d', 'c', 'h', 's', 'd']
        hand = Hand([Card(suits[i], ranks[i]) for i in range(5)])

        assert hand.valueAsText == "Full House"

    def test_fourOfAKind(self):
        ranks = [4, 4, 4, 4, 13]
        suits = ['d', 'c', 'h', 's', 'd']
        hand = Hand([Card(suits[i], ranks[i]) for i in range(5)])

        assert hand.valueAsText == "Four of a kind"

    def test_straightFlush(self):
        ranks = [1, 2, 3, 4, 5]
        suits = ['d', 'd', 'd', 'd', 'd']
        hand = Hand([Card(suits[i], ranks[i]) for i in range(5)])

        assert hand.valueAsText == "Straight flush"

    def test_royalFlush(self):
        ranks = [1, 10, 11, 12, 13]
        suits = ['d', 'd', 'd', 'd', 'd']
        hand = Hand([Card(suits[i], ranks[i]) for i in range(5)])

        assert hand.valueAsText == "Royal flush"

class TestStraight:
    def test_straight(self):
        ranks = [1,2,3,4,5]
        suits = ['d', 'c', 'h', 's']
        hand = Hand([Card(suits[random.randint(0, 3)], ranks[i]) for i in range(5)])

        assert hand.isStraight() == True

    def test_straightEdgeCase(self):
        ranks = [10, 11, 12, 13, 1]
        suits = ['d', 'c', 'h', 's']
        hand = Hand([Card(suits[random.randint(0, 3)], ranks[i]) for i in range(5)])

        assert hand.isStraight() == True


class TestHighCard:
    def test_sighCardWithoutAce(self):
        ranks = [3, 7, 11, 4, 5]
        suits = ['d', 'c', 'h', 's']
        hand = Hand([Card(suits[random.randint(0, 3)], ranks[i]) for i in range(5)])

        assert hand.highCard() == 11

    def test_sighCardWithAce(self):
        ranks = [1,7,4,6,12]
        suits = ['d', 'c', 'h', 's']
        hand = Hand([Card(suits[random.randint(0, 3)], ranks[i]) for i in range(5)])

        assert hand.highCard() == 14


def test_Flush():
    ranks = [1, 7, 11, 4, 5]
    suit = 'd'
    hand = Hand([Card(suit, ranks[i]) for i in range(5)])

    assert hand.isFlush() == True


class TestRoyalFlush:
    def test_RoyalFlush(self):
        ranks = [10, 11, 12, 13, 1]
        suit = 's'
        hand = Hand([Card(suit, ranks[i]) for i in range(5)])

        assert hand.isRoyalFlush() == True

    def test_royalFlushShouldFail(self):
        ranks = [1, 2, 3, 4, 5]
        suit = 'c'
        hand = Hand([Card(suit, ranks[i]) for i in range(5)])

        assert hand.isRoyalFlush() == False


def test_straightFlush():
    ranks = [1, 2, 3, 4, 5]
    suit = 'c'
    hand = Hand([Card(suit, ranks[i]) for i in range(5)])

    assert hand.isStraightFlush() == True

class TestFourOfAKind:
    def test_fourOfAKind(self):
        ranks = [2, 2, 2, 2, 5]
        suits = ['d','s','c','h','d']
        hand = Hand([Card(suits[i], ranks[i]) for i in range(5)])

        assert hand.isFourOfAKind() == True

    def test_fullHouseNotFourOfAKind(self):
        ranks = [3, 3, 3, 7, 7]
        suits = ['d', 's', 'c', 'h', 'd']
        hand = Hand([Card(suits[i], ranks[i]) for i in range(5)])

        assert hand.isFourOfAKind() == False

    def test_fourOfAkindBug(self):
        ranks = [2, 2, 3, 4, 5]
        suit = ['d', 'c', 'd', 's', 'd']
        hand = Hand([Card(suit[i], ranks[i]) for i in range(5)])

        assert hand.isFourOfAKind() == False


class TestFullHouse:
    def test_fullHouse(self):
        ranks = [3, 3, 3, 7, 7]
        suits = ['d', 's', 'c', 'h', 'd']
        hand = Hand([Card(suits[i], ranks[i]) for i in range(5)])

        assert hand.isFullHouse() == True

    def test_twoPairNotFullHouse(self):
        ranks = [3, 3, 3, 7, 2]
        suits = ['d', 's', 'c', 'h', 'd']
        hand = Hand([Card(suits[i], ranks[i]) for i in range(5)])

        assert hand.isFullHouse() == False

    def test_fullHouseRecognizedAsHighCard(self):
        ranks = [6, 6, 11, 11, 11]
        suits = ['h', 'd', 's', 'd', 'h']
        hand = Hand([Card(suits[i], ranks[i]) for i in range(5)])

        assert hand.isFullHouse() == True

class TestThreeOfAKind:
    def test_threeOfAKind(self):
        ranks = [7, 7, 7, 4, 5]
        suits = ['d', 'c', 'h', 's']
        hand = Hand([Card(suits[random.randint(0, 3)], ranks[i]) for i in range(5)])

        assert hand.isThreeOfAKind() == True

    def test_twoPairNotThreeOfAKind(self):
        ranks = [7, 7, 4, 4, 5]
        suits = ['d', 'c', 'h', 's','d']
        hand = Hand([Card(suits[i], ranks[i]) for i in range(5)])

        assert hand.isThreeOfAKind() != True

class TestTwoPair:
    def test_twoPair(self):
        ranks = [7, 7, 4, 4, 5]
        suits = ['d', 'c', 'h', 's', 'd']
        hand = Hand([Card(suits[i], ranks[i]) for i in range(5)])

        assert hand.isTwoPair() == True

    def test_notTwoPair(self):
        ranks = [1, 2, 3, 4, 5]
        suits = ['d', 'c', 'h', 's']
        hand = Hand([Card(suits[random.randint(0, 3)], ranks[i]) for i in range(5)])

        assert hand.isTwoPair() == False