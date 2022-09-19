import sys

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())

    coin = []

    for _ in range(n):
        coin.append(int(sys.stdin.readline()))

    coin.sort(reverse=True)

    count = 0
    for c in coin:
        if c > k:
            continue
        count += k // c
        k = k % c

    print(count)

