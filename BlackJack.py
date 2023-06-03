N, M = map(int, input().split())
card = list(map(int, input().split()))

good_card = 0
card_len = len(card)

for i in range(card_len - 2):
    for j in range(i + 1, card_len - 1):
        for k in range(j + 1, card_len):
            total = card[i] + card[j] + card[k]
            if total <= M and total > good_card:
                good_card = total

print(good_card)