# DFS는 stack으로, BFS는 queue로 구현

from collections import deque

def DFS(graph, v):
    visited = []
    stack = [v]

    while len(stack) != 0:
        a = stack.pop()
        if a not in visited:
            visited.append(a)
            if a in graph:
                temp = list(set(graph[a]) - set(visited))
                temp.sort(reverse=True)
                stack += temp

    for i in visited:
        print(i, end=" ")
    print()

def BFS(graph, v):
    visited = []
    q = deque([v])

    while len(q) != 0:
        a = q.popleft()
        if a not in visited:
            visited.append(a)
            if a in graph:
                temp = list(set(graph[a]) - set(visited))
                temp.sort()
                q += temp

    for i in visited:
        print(i, end=" ")

n, m, v = map(int, input().split())
graph = {}

for i in range(m):  # 그래프 딕셔너리
    n1, n2 = map(int, input().split())

    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

DFS(graph, v)
BFS(graph, v)