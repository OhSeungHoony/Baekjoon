import sys
"""
오답 1
k, p, n = map(int, sys.stdin.readline().split())
print(k*(p**n)%1000000007)
"""

k, p, n = map(int, sys.stdin.readline().split())

# 나머지 성질 이용
for i in range(n):
    k = (k * p) % 1000000007
print(k)
