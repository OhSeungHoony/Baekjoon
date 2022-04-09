import sys

def solution(m, n):
    numbers = [False, False] + [True]*(n-1)
    primes = []

    for i in range(2, n+1):
        if numbers[i]:
            if i < m:
                pass
            else:
                primes.append(i)
            for j in range(2*i, n+1, i):
                numbers[j] = False

    for prime in primes:
        print(prime)

if __name__ == "__main__":
    m, n = map(int, sys.stdin.readline().split())
    solution(m, n)