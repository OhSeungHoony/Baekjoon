import sys
from collections import Counter

def solution(numbers, n):
    numbers.sort()
    ans = []

    print(round(sum(numbers)/n)) # 산술평균

    print(numbers[(n-1)//2]) # 중앙값

    c = Counter(numbers).most_common() # 최빈값
    if n > 1:
        if c[0][1] == c[1][1]:
            print(c[1][0])
        else:
            print(c[0][0])
    else:
        print(c[0][0])

    print(max(numbers)-min(numbers)) # 최대최소차이



if __name__ == "__main__":
    n = int(sys.stdin.readline())
    numbers = []

    for _ in range(n):
        num = int(sys.stdin.readline())
        numbers.append(num)
    solution(numbers, n)
