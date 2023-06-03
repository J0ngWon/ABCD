N, K = map(int, input().split())  

##print('%d %d \n'%(N,K))  


gazi = []  

for x in range(N):
    coin = int(input())
    gazi.append(coin)

count = 0  
for i in range(N - 1, -1, -1):  
    if K >= gazi[i]: 
        count += K // gazi[i] 
        K %= gazi[i] 
    if K == 0: 
        break

print(count) 

