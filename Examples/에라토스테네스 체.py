"""
    에라토스테네스의 체를 이용하여 n 이하의 소수 출력
"""
import sys

def solution(n):
    board = [False, False] + [True]*(n-1)
    primes = []

    for i in range(2, n+1):
        if board[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                board[j] = False

    return primes

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(solution(n))