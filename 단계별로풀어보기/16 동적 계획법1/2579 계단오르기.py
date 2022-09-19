"""
테이블 정의하기
D[i][j] = 현재까지 j개의 계단을 연속해서 밟고 i번째 계단까지 올라섰을 때 점수 합의 최댓값, 단 i 번째 계단은 반드시 밟아야 함.
이 때 3개의 계단을 연속해서 밟을 수 없으므로 j = 1 or j = 2 여야 함.
"""
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    score = []
    D = []
    for _ in range(n):
        score.append(int(sys.stdin.readline()))
        D.append([0, 0])
    for i in range(n):
        if i == 0:
            D[i][0] = score[0]
            D[i][1] = 0
        elif i == 1:
            D[i][0] = score[1]
            D[i][1] = score[0] + score[1]
        else:
            D[i][0] = max(D[i-2][0], D[i-2][1]) + score[i]
            D[i][1] = D[i-1][0] + score[i]
    print(max(D[n-1][0], D[n-1][1]))