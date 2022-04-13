import sys

def isPrime(m, n):
    numbers = [False, False] + [True] * (n - 1)
    prime_cnt = 0

    for i in range(2, n + 1):
        if numbers[i]:
            if i <= m:
                pass
            else:
                prime_cnt += 1
            for j in range(2 * i, n + 1, i):
                numbers[j] = False
    return prime_cnt

def solution(numbers):
    for num in numbers:
        print(isPrime(num, num*2))

if __name__ == "__main__":
    numbers = []
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            break
        else:
            numbers.append(n)
    solution(numbers)