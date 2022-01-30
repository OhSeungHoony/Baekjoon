""" 우선순위 큐 사용
import queue
import sys

n = int(sys.stdin.readline())
que = queue.PriorityQueue()
list = []

for i in range(n):
    x = int(sys.stdin.readline().strip())
    if x == 0 and que.empty():
        list.append(0)
    elif x == 0:
        list.append(que.get())
    else:
        que.put(x)

for data in list:
    print(data)
"""
""" heapq 모듈 사용 """
import heapq
import sys

n = int(sys.stdin.readline())
q = []
list = []
for i in range(n):
    x = int(sys.stdin.readline().strip())
    if x > 0:
        heapq.heappush(q, x)
    elif x == 0:
        if len(q) == 0:
            list.append(0)
        else:
            list.append(heapq.heappop(q))

for data in list:
    print(data)