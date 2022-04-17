import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    D = [0]*(n+1)
    numbers = [0]*(n+1)
    cnt = []
    for i in range(2, n + 1):
        D[i] = D[i - 1] + 1
        numbers[i] = i - 1
        if i % 2 == 0 and D[i] > D[i//2] + 1:
            D[i] = D[i // 2] + 1
            numbers[i] = i // 2
        if i % 3 == 0 and D[i] > D[i//3] + 1:
            D[i] = D[i // 3] + 1
            numbers[i] = i // 3

    print(D[n])
    while True:
        print(n, end=" ")
        if n == 1:
            break
        n = numbers[n]
