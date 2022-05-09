import sys
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i]:
                pass
            else:
                queue.append(i)
                visited[i] = True
    return visited

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = bfs(graph, 1, visited)
    cnt = 0
    for v in visited:
        if v:
            cnt += 1
    print(cnt - 1)
