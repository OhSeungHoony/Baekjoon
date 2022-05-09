"""
    문제 똑바로 읽자 오름차순 빼먹어서 틀렸다.
"""
import sys
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    area = 1
    board[x][y] = '0'
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if board[nx][ny] == '1':
                queue.append((nx, ny))
                board[nx][ny] = '0'
                area += 1
    result.append(area)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    board = [list(sys.stdin.readline()[:-1]) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    result = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == '1':
                bfs(i, j)

    print(len(result))
    result.sort()
    for i in range(len(result)):
        if i == len(result)-1:
            print(result[i], end="")
        else:
            print(result[i])