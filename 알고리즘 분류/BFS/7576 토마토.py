from collections import deque

m, n = map(int, input().split())
board = []
ans = 0
for _ in range(n):
    b = list(map(int, input().split()))
    for bb in b:
        if bb == 0:
            ans += 1
            break
    board.append(b)

day = 0

q = deque(())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i, j))

while q:
    day += 1
    for _ in range(len(q)):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny] == 0:
                    board[nx][ny] = 1
                    q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            ans = -1

if ans == 0:
    print(ans)
elif ans == -1:
    print(ans)
else:
    print(day - 1)