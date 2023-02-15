import sys

n = int(sys.stdin.readline())
list_1 = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())
cnt = 0
for num in list_1:
    if num == v: cnt += 1
print(cnt)