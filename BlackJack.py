N, M = map(int, input().split())
card = list(map(int, input().split()))

##print('%d %d \n'%(N,M))   
'''for k in range(N): 
    print('생성된 %d번째 카드 숫자=%d'%(k+1,card[k]))  
    print('\n') ''' 


good_card = 0
card_len = len(card)

for i in range(card_len - 2):
    for j in range(i + 1, card_len - 1):
        for k in range(j + 1, card_len):
            total = card[i] + card[j] + card[k]
            if total <= M and total > good_card:
                good_card = total

print(good_card)

'''count=int(0)
result_card=[]
card_len=len(card)     
good_card=int(card[0]+card[1]+card[2])
q=2
r=1

for i in range(card_len-2):
    for j in range(r,card_len-1):
        if j+1==card_len:
            r+=1
        for k in range(q,card_len):
            result_card.append(card[i]+card[j]+card[k])
            if abs(M-result_card[count])>=abs(M-good_card):
                good_card=result_card[count]
           
            if k+1==card_len:
                q+=1
            count+=1
print('%d'%(good_card))'''   