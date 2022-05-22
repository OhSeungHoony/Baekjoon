import sys
from collections import deque

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    board = []

    for _ in range(n):
        board.append(list(map(int, sys.stdin.readline().split())))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                queue.append((i, j))

    year = 0

    while True:
        visited = [[0] * m for _ in range(n)]
        for x in range(n):
            for y in range(m):
                if board[x][y] != 0:
                    cnt = 0
                    visited[x][y] = 1
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0<=nx<n and 0<=ny<m and board[nx][ny]==0 and visited[nx][ny]==0:
                            cnt += 1
                    if board[x][y] - cnt <= 0:
                        board[x][y] = 0
                    else:
                        board[x][y] -= cnt
        year += 1
        cnt = 0
        for x in range(n):
            for y in range(m):
                if visited[x][y] != 0:
                    cnt += 1
                    queue = deque()
                    queue.append((x, y))
                    while queue:
                        x, y = queue.popleft()
                        for i in range(4):
                            nx = x + dx[i]
                            ny = y + dy[i]
                            if 0<=nx<n and 0<=ny<m and visited[nx][ny] != 0:
                                visited[nx][ny] = 0
                                queue.append((nx, ny))

        if cnt == 0:
            print(0)
            break
        if cnt >= 2:
            print(year - 1)
            break
