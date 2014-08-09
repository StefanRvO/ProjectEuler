#!/usr/bin/python
# -*- coding: utf-8 -*-
#Datastructure:
#A hand o five crads is put in to a list of lists e.g.:
#[[5,D],[11,S],[12,D],[4,H],[7,D]]
#D=Diamonds/ruder,C=clubs/klør,H=Hearts/hjerter,S=spades/spar
#T=Teen/10,#J=Jack/11,#Q=Queen/12,#K=King/13,#A=Ace/14
def LoadHands():
    file=open('poker.txt')
    handsraw=file.readlines()
    hands=[]
    for i in xrange(len(handsraw)):
        handsraw[i]=handsraw[i].split(" ")
        handsraw[i][-1]=handsraw[i][-1][:2]
        hands.append([handsraw[i][:5],handsraw[i][5:]])
        for j in xrange(len(hands[i])):
            for k in xrange(len(hands[i][j])):
                card=hands[i][j][k]
                hands[i][j][k]=[]
                if card[0]=='T':
                    hands[i][j][k].append(10)
                elif card[0]=='J':
                    hands[i][j][k].append(11)
                elif card[0]=='Q':
                    hands[i][j][k].append(12)
                elif card[0]=='K':
                    hands[i][j][k].append(13)
                elif card[0]=='A':
                    hands[i][j][k].append(14)
                else:
                    hands[i][j][k].append(int(card[0]))
                hands[i][j][k].append(card[1])
    return hands
def HighCard(Deck,number=1): #Return the higest card. if number is not 1, the n'th highest crad will be returned
    #Clean for suits, only want values
    Cards=[card[0] for card in Deck]
    return sorted(Cards,reverse=True)[number-1]
def Pairs(Deck): #Return how many pairs is in the deck
    #Clean for suits, only want values
    Cards=[card[0] for card in Deck]
    Pairs=0
    for card in Cards:
        if Cards.count(card)==2:
            Cards.remove(card)
            Cards.remove(card)
            Pairs+=1
    return Pairs
def GetPair(Deck,number=1): #Return the higest card. if number is not 1, the n'th highest crad will be returned
    #Clean for suits, only want values
    Cards=[card[0] for card in Deck]
    Pairs=[]
    for card in Cards:
        if Cards.count(card)==2:
            Cards.remove(card)
            Cards.remove(card)
            Pairs.append(card)
    if number>len(Pairs):
        raise Exception("The Pair Requsted don't exist in deck")
    return sorted(Pairs)[-number]
def ThreeOfAKind(Deck):
    #Clean for suits, only want values
    Cards=[card[0] for card in Deck]
    for card in Cards:
        if Cards.count(card)==3:
            return card
    return False
def Straight(Deck):
    #Clean for suits, only want values
    Cards=[card[0] for card in Deck]
    Cards.sort()
    for i in xrange(4):
        if not Cards[i]==Cards[i+1]-1:
            return False
    return Cards[-1]
def Flush(Deck):
    for i in range(4):
        if not Deck[i][1]==Deck[i+1][1]:
            return False
    else:
        return max([card[0] for card in Deck])
def FullHouse(Deck):
    three=ThreeOfAKind(Deck)
    if three:
         if Pairs(Deck):
            return three
    return False
def FourOfAKind(Deck):
    Cards=[card[0] for card in Deck]
    for card in Cards:
        if Cards.count(card)==4:
            return card
    return False
def StraightFlush(Deck):
    if Flush(Deck):
        return Straight(Deck)
def BestHand(Deck1,Deck2):
    if StraightFlush(Deck1) or StraightFlush(Deck2):
        if StraightFlush(Deck1)>StraightFlush(Deck2):
            return 1
        else:
            return 2
    if FourOfAKind(Deck1) or FourOfAKind(Deck2):
        if StraightFlush(Deck1)>StraighFlush(Deck2):
            return 1
        else:
            return 2
    if FullHouse(Deck1) or FullHouse(Deck2):
        if FullHouse(Deck1)>FullHouse(Deck2):
            return 1
        else:
            return 2
    if Flush(Deck1) or Flush(Deck2):
        if Flush(Deck1)>Flush(Deck2):
            return 1
        else:
            return 2
    if Straight(Deck1) or Straight(Deck2):
        if Straight(Deck1)>Straight(Deck2):
            return 1
        else:
            return 2
    if ThreeOfAKind(Deck1) or ThreeOfAKind(Deck2):
        if ThreeOfAKind(Deck1)>ThreeOfAKind(Deck2):
            return 1
        elif ThreeOfAKind(Deck1)<ThreeOfAKind(Deck2):
            return 2
    if Pairs(Deck1) or Pairs(Deck2):
        if Pairs(Deck1)>Pairs(Deck2):
            return 1
        elif Pairs(Deck1)<Pairs(Deck2):
            return 2
        else:
            pairs=Pairs(Deck1)
            for i in range(1,pairs+1):
                if GetPair(Deck1,i)>GetPair(Deck2,i):
                    return 1
                elif GetPair(Deck1,i)<GetPair(Deck2,i):
                    return 2
            
    for i in xrange(1,6):
        if HighCard(Deck1,i)>HighCard(Deck2,i):
            return 1
        elif HighCard(Deck1,i)<HighCard(Deck2,i):
            return 2
        else:
            continue

hands=LoadHands() 
player1wins=0
for hand in hands:
    if BestHand(hand[0],hand[1])==1:
        player1wins+=1
print player1wins     
    

