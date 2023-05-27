import random
import math

'''def combination(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
'''
N=int(input())  #카드수 3~10
M=int(input())  #최대수 10~300
card=[]

for k in range(N):
    card_number=int(random.randint(1, M))
    
    card.append(card_number)
    print('생성된 %d번째 카드 숫자=%d'%(k+1,card[k]))  
    print('\n')   



'''for k in range(N):
    if card[k]>=M :
        del(card[k])'''

count=int(0)
result_card=[]
card_len=len(card)     
'''combination(card_len,3) #총 반복 횟수 조합이용 (nCr)'''

good_card=int(card[0]+card[1]+card[2])
q=2
r=1

for i in range(card_len-2):
    for j in range(r,card_len):
        if j-1==card_len:
            r+=1
        for k in range(q,card_len):
            result_card.append(card[i]+card[j]+card[k])
            if abs(M-result_card[count])<=abs(M-good_card):
                good_card=result_card[count]
           
            if k-1==card_len:
                q+=1
            count+=1
print('제출값=%d'%(good_card))   
       