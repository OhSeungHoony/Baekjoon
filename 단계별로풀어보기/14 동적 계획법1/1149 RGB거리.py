# D[i][0] -> i번째 집까지 칠할 때 비용의 최솟값, i번째 집은 빨강
# D[i][1] -> i번째 집까지 칠할 때 비용의 최솟값, i번째 집은 초록
# D[i][2] -> i번째 집까지 칠할 때 비용의 최솟값, i번째 집은 파랑
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    priceAll = []
    D = []
    for _ in range(n):
        priceAll.append(list(map(int, sys.stdin.readline().split())))
        D.append([0, 0, 0])

    for i in range(n):
        if i == 0:
            D[i][0] = priceAll[0][0]
            D[i][1] = priceAll[0][1]
            D[i][2] = priceAll[0][2]
        else:
            D[i][0] = min(D[i - 1][1], D[i - 1][2]) + priceAll[i][0]
            D[i][1] = min(D[i - 1][0], D[i - 1][2]) + priceAll[i][1]
            D[i][2] = min(D[i - 1][0], D[i - 1][1]) + priceAll[i][2]

    print(int(min(D[n-1][0], D[n-1][1], D[n-1][2])))