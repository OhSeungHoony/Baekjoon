import sys
"""
    D[i] = 2 * i 크기의 직사각형을 채우는 방법의 수
    D[i] = D[i-1] + D[i-2]
"""
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    if n < 3:
        print(n)
    else:
        D = [0]*n
        D[0] = 1
        D[1] = 2
        for i in range(2, n):
            D[i] = D[i-1] + D[i-2]
        print(D[-1] % 10007)