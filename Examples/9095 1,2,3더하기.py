import sys
"""
    D[i] = i를 1, 2, 3의 합으로 나타낸 방법의 수
    D[1] = 1
    D[2] = 2
    D[3] = 4
    D[4] = 7
    D[5] = 13
"""

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    num = []
    for _ in range(n):
        x = int(sys.stdin.readline())
        num.append(x)
    D = list(0 for _ in range(max(num)+1))
    D[0] = 1
    D[1] = 1
    D[2] = 2
    for i in range(3, max(num)+1):
        D[i] = D[i-3] + D[i-2] + D[i-1]
    for x in num:
        print(D[x])