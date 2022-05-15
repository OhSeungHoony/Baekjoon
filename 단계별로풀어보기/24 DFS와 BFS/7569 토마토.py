import sys
from collections import deque

def solution(b):
    day = 0
    for i in b:
        for j in i:
            for k in j:
                day = max(day, k - 1)
                if k == 0:
                    return print(-1)
    print(day)


if __name__ == "__main__":
    m, n, h = map(int, sys.stdin.readline().split())
    board = []
    for _ in range(h):
        b = []
        for _ in range(n):
            b.append(list(map(int, sys.stdin.readline().split())))
        board.append(b)

    queue = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if board[i][j][k] == 1:
                    queue.append([i, j, k])

    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    while queue:
        z, y, x = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                if board[nz][ny][nx] == 0:
                    board[nz][ny][nx] = board[z][y][x] + 1
                    queue.append([nz, ny, nx])

    solution(board)