# n 이하의 정수 중 소수를 출력
import sys

def solution(n):
    numbers = [False, False] + [True]*(n-1)
    primes = []

    for i in range(2, n+1):
        if numbers[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                numbers[j] = False

    return primes

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(solution(n))