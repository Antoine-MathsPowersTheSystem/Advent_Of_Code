# -*- coding: utf-8 -*-

import pandas as pd
import time

#%% FUNCTIONS
def generate_type_hand(key,set_cards):
    def intern_type_hand(hand):
        hand_sort=''.join(sorted(hand, key=order))
    
        for card in set_cards:
            if card*5 in hand_sort: return 6
    
        for card in set_cards:
            if card*4 in hand_sort: return 5
    
        for card in set_cards:
            if card*3 in hand_sort:
                for card2 in set_cards:
                    if card!=card2 and card2*2 in hand_sort: return 4
                return 3
    
        for card in set_cards:
            if card*2 in hand_sort:
                for card2 in set_cards:
                    if card != card2 and card2*2 in hand_sort: return 2
                return 1
    
        return 0
    return intern_type_hand


def generate_hand_to_int( set_cards):
    return lambda hand: sum([(set_cards.find(char)+1)*len(set_cards)**i for i,char in enumerate(hand[::-1])])

def generate_order(set_cards):
    return lambda card:set_cards.find(card)


def generate_order2(set_cards,hand_to_int):
    return lambda item: (-item[0],hand_to_int(item[1]))

tperf0=time.time()

df = pd.read_csv('input.txt', header=None, sep=" ")
hands = df[0].to_list().copy()
values = df[1].to_list().copy()
all_cards = 'AKQJT98765432'

tperf1=time.time()
#%% PART 1
#Generate function
hand_to_int=generate_hand_to_int( all_cards)
order=generate_order(all_cards)
order2= generate_order2(all_cards,hand_to_int)
type_hand=generate_type_hand(order,all_cards)

games=[ (type_hand(i),i,j) for i,j in zip(hands,values)]
games_sort=sorted(games,key=order2)
S=0
for i,hand_loop in enumerate(games_sort[::-1]):
    S+= hand_loop[2]*(i+1)
print("solution 2:",S)
#250474325

tperf2=time.time()
#%%PART 2
all_cards2= 'AKQT98765432J'
hand_to_int=generate_hand_to_int( all_cards2)
order=generate_order(all_cards2)
order2= generate_order2(all_cards2,hand_to_int)
type_hand=generate_type_hand(order,all_cards2)


def maximise_hand(game):
    hand=game[2]
    if not('J' in hand):
        return type_hand(game[2]),game[1],game[2],game[3]
    elif True:
        J_pos=hand.find('J')
        type_hand_res=type_hand(hand)
        l=[]
        for card in all_cards2[::-1][1:]:
            temp_hand=list(hand)
            temp_hand[J_pos]=card
            temp_hand=''.join(temp_hand)
            l.append(maximise_hand((type_hand(temp_hand),game[1],temp_hand,game[3]))[0])
        if max(l)>=game[0]:
            pos_max=l.index(max(l))
            temp_hand=list(hand)
            temp_hand[J_pos]=all_cards2[::-1][1:][pos_max]
            temp_hand=''.join(temp_hand)
            return max(l),game[1],temp_hand,game[3]
        return game
    


games2=[ maximise_hand((type_hand(i),i,i,j)) for i,j in zip(hands,values)]
games2_sort=sorted(games2,key=order2)
S=0
for i,game in enumerate(games2_sort[::-1]):
    S+= game[3]*(i+1)
    
tperf3=time.time()    
    
print("solution 1:",S)
# 249010224 to high
# 248883200
# 248971087
# 248941301
# 249072540
print("time  read:",round(tperf1-tperf0,6),"s")
print("time part1:",round(tperf2-tperf1,6),"s")
print("time part2:",round(tperf3-tperf2,6),"s")
print("time   tot:",round(tperf3-tperf0,6),"s")


