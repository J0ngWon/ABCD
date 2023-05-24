import random
N=int(input())  #카드수 3~10
M=int(input())  #최대수 10~300
card=[]

for k in range(N):
    card_number=int(random.randint(1, M))
    if card_number in card :
        N-=1
        continue
    card.append(card_number)
    print('생성된 %d번째 카드 숫자=%d'%(k+1,card[k]))  
    print('\n')   

