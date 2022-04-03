n, k = map(int, input().split())

coin = []
count = []
for _ in range(n):
    coin_won = int(input())
    coin.append(coin_won)
coin.sort(reverse=True)
for i in range(n):
    if coin[i] > k:
        continue
    count.append(k // coin[i])
    k = k % coin[i]

print(sum(count))
