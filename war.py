from random import shuffle
import time

def printDeck(deck):
    for card in deck:
        print(card)

def compareCards(p1Card, p2Card):
    if(p1Card[2] > p2Card[2]):
        print("P2's " + str(p2Card) + " lost to P1's " + str(p1Card) + "!")
        return("p1")
    elif(p2Card[2] > p1Card[2]):
        print("P1's " + str(p1Card) + " lost to P2's " + str(p2Card) + "!")
        return("p2")
    else:
        print("Tie!")
        return("tie")

def manipulateDeck(p1d, p2d, p1Card, p2Card):
    rslt = compareCards(p1Card, p2Card)
    
    p1NewDeck = p1d
    p2NewDeck = p2d

    if(rslt == "p1"):
        p1NewDeck.remove(p1Card)
        p2NewDeck.remove(p2Card)
        
        p1NewDeck.append(p1Card)
        p1NewDeck.append(p2Card)

    elif(rslt == "p2"):
        p1NewDeck.remove(p1Card)
        p2NewDeck.remove(p2Card)
        
        p2NewDeck.append(p1Card)
        p2NewDeck.append(p2Card)
    elif(rslt == "tie"):
        for i in range(4):
            p1NewDeck.pop(0)
            p2NewDeck.pop(0)

        p1NumCardsBefore = len(p1NewDeck)

        newDecks = manipulateDeck(p1NewDeck, p2NewDeck, p1NewDeck[0],p2NewDeck[0])

        p1NewDeck = newDecks[0]
        p2NewDeck = newDecks[1]

        if(len(p1NewDeck) > p1NumCardsBefore):
            # p1 has won somewhere
            # p1 gets the tie cards
            p1NewDeck.append(p1Card)
            p1NewDeck.append(p2Card)
        else:
            # p2 has won somewhere
            # p2 gets the tie cards
            p2NewDeck.append(p1Card)
            p2NewDeck.append(p2Card)
    else:
        print("wat")

    return([p1NewDeck, p2NewDeck])

def gameTick(players):
    p1d = players[0]
    p2d = players[1]

    p1Card = p1d[0]
    p2Card = p2d[0]

    players = manipulateDeck(p1d, p2d, p1Card, p2Card)


# initializing stuff ot inizialize the cards
suits = ["clubs", "diamonds", "spades", "hearts"]
numbers = []
for i in range(2, 11):
    numbers.append((str(i), i))
numbers.append(("jack",11))
numbers.append(("queen",12))
numbers.append(("king",13))
numbers.append(("ace",14))

# maek dek
deck = []
for suit in suits:
    for number in numbers:
        deck.append((number[0], suit, number[1]))

shuffle(deck)

print("Deck is ready.")

print("len deck = " + str(len(deck)))

numPlayers = 2
player1Deck = deck[0:int(len(deck)/numPlayers)]
player2Deck = deck[int(len(deck)/numPlayers):len(deck)]

print("player 1 has " + str(len(player1Deck)) + " cards")
print("player 2 has " + str(len(player2Deck)) + " cards")

players = [player1Deck, player2Deck]

while(True):

    print("player 1 has " + str(len(player1Deck)) + " cards")
    print("player 2 has " + str(len(player2Deck)) + " cards")

    if(len(players[0]) == 0 or len(players[1]) == 0):
        break;

    gameTick(players)

    #time.sleep(.5)

# figure out who wins
if(len(players[0]) == 0):
    print("Player 1 wins yo")
elif(len(players[1]) == 0):
    print("Player 2 wins yo")
else:
    print("Wtf yo")
