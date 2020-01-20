import sys

from Models.Dealer import Dealer

#Dealer constructor takes the amount of players, if empty default is 3 and max is 10.
dealer = Dealer(3)

if len(sys.argv) > 1:
    if "generate" in sys.argv[1]:
        dealer.frequencyTableOfHandDistribution(10)
else:
    dealer.dealToPlayers()

