from functools import lru_cache
# LRU(Least Recently Used) 캐시에 가장 최근까지 적게 사용된 장소에 재귀함수 계산값을 저장해놨다가 빠르게 불러와 쓸 수 있게 해줌
# 메모아이제이션(memoization)

t = int(input())

for _ in range(t):
    @lru_cache()
    def S(k, n):
        if k == 0:
            return n
        else:
            sum = 0
            for i in range(1, n+1):
                sum += S(k-1, i)
            return sum
    k = int(input())
    n = int(input())
    print(S(k, n))