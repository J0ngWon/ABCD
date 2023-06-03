N, K = map(int, input().split())  

gazi = []  

for _ in range(N):
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

