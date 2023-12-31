deck_list=input().split(' ')
shuffle_count=int(input())

for i in range(shuffle_count):
    shuffled_deck=[]
    sub_deck_a=deck_list[0:int(len(deck_list)/2)]
    sub_deck_b=deck_list[int(len(deck_list)/2):]
    for j in range(len(sub_deck_a)):
        shuffled_deck.append(sub_deck_a[j])
        shuffled_deck.append(sub_deck_b[j])
    deck_list=shuffled_deck[:]

print(deck_list)