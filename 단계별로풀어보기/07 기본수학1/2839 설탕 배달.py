import sys

def solution(n):
    count = 0
    while True:
        if n % 5 == 0:
            count += n // 5
            break
        count += 1
        n -= 3
        if n == 0:
            break
        if 0 > n:
            count = -1
            break
    return count

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(solution(n))
