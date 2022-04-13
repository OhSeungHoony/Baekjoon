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