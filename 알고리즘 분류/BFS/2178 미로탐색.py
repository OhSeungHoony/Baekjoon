from collections import deque

n, m = map(int, input().split())
board = []
for i in range(n):
    number = input()
    b = []
    for j in range(m):
        b.append(int(number[j]))
    board.append(b)

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((x, y))

    while True:
        if len(q) == 0:
            break
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))

    return board[n-1][m-1]

print(bfs(0, 0))
