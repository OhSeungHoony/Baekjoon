# 하노이 탑
import sys

def solution(n, start, temp, to):
    if n == 1:
        print(start, to)
    else:
        solution(n-1, start, to , temp)
        print(start, to)
        solution(n-1, temp, start, to)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(2**n-1)
    solution(n, 1, 2, 3)